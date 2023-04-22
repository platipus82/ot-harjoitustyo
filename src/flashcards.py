#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 17 Apr 2023

@author: olegk
'''
import os
#import pygame
#import random
#import math
#import time

#import sys

class App:
    def __init__(self, use_default_input=True, output_allowed=False):
        self.default_input=use_default_input
        self.output_allowed=output_allowed
        self.input_dir = ""
        self.input_path = ""
        if not self.default_input: 
            self.__ui = UI(use_default_input=self.default_input, output_allowed=output_allowed)
        self.exit = False
        self.data = []
        self.filelist = []
        self.set_parameters()

    def set_parameters(self):
        self.set_input_dir()
        self.get_input_filelist()

        if self.default_input: # ==True
            self.set_input_path_default()
        else:
            self.set_input_path()
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
        if not self.default_input:
            resp = self.__ui.ask_for_input(output_text=filelist_description)
            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                self.exit = True
                return

    def set_input_path(self):
        pth= self.__ui.ask_for_input_file("") #GUI_input_file_selection()
        self.input_path = pth
        
    def set_input_path_v1(self):
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
        self.__exit = False
        self.game = App(use_default_input=False, output_allowed=True)
        self.__ui = UI(use_default_input=False, output_allowed=True)
        self.__exit=self.game.exit
        if self.__exit == False:
            self.ask()

    def ask(self):
        lst = self.game.data
        for i in range(0, len(lst)):
            y = lst[i].split(";")
            question = y[0]
            answer = y[1]
            msg_pt1 = "Please, press proceed to see the correct answer" + "\n"
            msg_pt2 = "Press exit to exit the application" + "\n"
            msg = "Question: " + question + "\n" + msg_pt1 + msg_pt2            
            resp = self.__ui.ask_for_input(output_text=msg)

            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                break
            msg = "Question: " + question + "\n" + "Answer: " + "\n" + answer + "\n"

            if i!=len(lst)-1:
                msg = msg + "Next question? "
                resp = self.__ui.ask_for_input(output_text=msg)
            else:
                msg = msg + "This was the last question! Well done!"
                self.__ui.show_output(output_text=msg)

            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                break

def main():
    Play()

if __name__ == "__main__":
    import os
    from ui.ui import UI  
    from ui.ui import GUI
    from ui.ui import GUI_input_file_selection

    main()