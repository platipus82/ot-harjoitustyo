#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 17 Apr 2023

@author: olegk
'''

#import pygame
#import random
#import math
#import time

#import sys
import os
from ui.ui import UI

class App:
    def __init__(self, use_default_input=True, output_allowed=False):
        self.default_input=use_default_input
        self.output_allowed=output_allowed
        self.input_dir = ""
        self.input_path = ""
        self.__ui = UI(use_default_input=self.default_input, output_allowed=output_allowed)
        self.data = []
        self.filelist = []
        self.set_parameters()

    def set_parameters(self):
        #print("Function set_parameters")
        self.set_input_dir()
        self.get_input_filelist()

        if self.default_input: # ==True
            #print("self.default_input==True")
            self.set_input_path_default()
        else:
            #print("self.default_input==False")
            self.set_input_path()

        #print("Input path received: " + self.input_path)
        self.get_input_data()

    def set_input_dir(self):
        self.input_dir = os.getcwd() + "\inputs\\"
        if not os.path.isdir(self.input_dir):
            self.input_dir = os.getcwd() + "/src/inputs//"


    def get_input_filelist(self):
        filelist = os.listdir(self.input_dir)
        filelist = [x for x in filelist if x.endswith(".csv") or x.endswith(".txt") ]
        self.filelist = filelist

    def set_input_path_default(self):
        filelist = self.filelist
        filelist_description = "Currently available files are: " + "\n"
        for i in range(0, len(filelist)):
            filepart =  str(i) + ": " + filelist[i] + "\n"
            filelist_description = filelist_description+filepart
        new_part = "Currently running in default input mode and will use the first available file."
        filelist_description = filelist_description + new_part
        self.input_path = self.input_dir + "/" + self.filelist[0]
        if not os.path.isfile(self.input_path):
            self.input_path = self.input_dir + "\\" + self.filelist[0]
        filelist_description = filelist_description + self.filelist[0]
        self.__ui.show_output(output_text=filelist_description)

    def set_input_path(self):
        #self.input_path = os.getcwd() + "\inputs\\"
        filelist = self.filelist
        filelist_description = "Currently available files are: " + "\n"
        for i in range(0, len(filelist)):
            filepart =  str(i) + ": " + filelist[i] + "\n"
            filelist_description = filelist_description+filepart
        new_part =  "Please, choose correct input file by typing the corresponding number..."
        filelist_description = filelist_description + new_part
        #print(filelist_description)

        while True:
            num = self.__ui.ask_for_input(output_text=filelist_description)
            try:
                num = int(num)
                if 0 <= num < len(filelist):
                    break
                else:
                    msg = "You must choose an integer between 0 and " + str(len(filelist))
                    self.__ui.show_output(output_text=msg)
            except ValueError:
                msg = "You must choose an integer between 0 and " + str(len(filelist))
                self.__ui.show_output(output_text=msg)
        #print(f"You have chosen file {filelist[num]} ({num})")
        msg = f"You have chosen file {filelist[num]} ({num})"
        self.__ui.show_output(output_text=msg)

        self.input_path = self.input_dir + "/" + filelist[num]
        if not os.path.isfile(self.input_path):
            self.input_path = self.input_dir + "\\" + filelist[num]

    def get_input_data(self):
        try:
            with open(self.input_path, "r", encoding="utf-8") as infile:
                lines = []
                i=0
                for line in infile:
                    if line != "" :
                        lines.append(line)
                        i += 1
                self.data = lines
                return True
        except OSError:
            return False

class Play:
    def __init__(self):
        self.game = App(use_default_input=False, output_allowed=True)
        self.__ui = UI(use_default_input=False, output_allowed=True)
        self.ask()

    def ask(self):
        lst = self.game.data
        for i in range(0, len(lst)):
            y = lst[i].split(";")
            question = y[0]
            answer = y[1]
            self.__ui.show_output(question)
            msg_pt1 = "Is your answer ready?"
            msg_pt2 = "Please, press x for exit "
            msg_pt3 = "or any other key to see the correct answer..."
            msg = msg_pt1 + msg_pt2 + msg_pt3
            #resp = input(msg)
            resp = self.__ui.ask_for_input(output_text=msg)

            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                break
            msg = answer
            self.__ui.show_output(output_text=msg)
            if i!=len(lst)-1:
                #resp = input("Next question? Press x for exit, or any other key to continue...")
                msg = "Next question? Press x for exit, or any other key to continue..."
                resp = self.__ui.ask_for_input(output_text=msg)

            else:
                msg = "This was the last question! Well done!"
                self.__ui.show_output(output_text=msg)
            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                break

def main():
    Play()

if __name__ == "__main__":
    main()
