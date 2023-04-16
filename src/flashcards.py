#!/usr/bin/python  
# -*- coding: utf-8 -*-
'''
Created on 16 Apr 2023

@author: olegk
'''
import pygame
import random
import math
import time

import sys
import os

class App:
    def __init__(self):
        self.input_dir = ""
        self.input_path = ""
        self.data = []
        self.set_input_dir()
        self.set_input_path()
        self.get_input_data()

    def set_input_dir(self):
        self.input_dir = os.getcwd() + "\inputs\\"
        if not os.path.isdir(self.input_dir):
            self.input_dir = os.getcwd() + "/src/inputs//"

    def set_input_path(self):
        #self.input_path = os.getcwd() + "\inputs\\"
        filelist = os.listdir(self.input_dir)
        filelist = [x for x in filelist if x.endswith(".csv") or x.endswith(".txt") ]
        filelist_description = "Currently available files are: " + "\n"
        for i in range(0, len(filelist)):
            filepart =  str(i) + ": " + filelist[i] + "\n"
            filelist_description = filelist_description+filepart
        filelist_description = filelist_description + "Please, choose correct input file by typing the corresponding number..."
        print(filelist_description)

        while True:
            num = input(filelist_description)
            try:
                num = int(num)
                if 0 <= num < len(filelist):
                    break
                else:
                    print("You must choose an integer between 0 and " + str(len(filelist)))
            except:
                print("You must choose an integer between 0 and " + str(len(filelist)))
        print(f"You have chosen file {filelist[num]} ({num})") 

        self.input_path = self.input_dir + "/" + filelist[num]
        if not os.path.isfile(self.input_path): 
            self.input_path = self.input_dir + "\\" + filelist[num]

    def get_input_data(self): 
            try:
                infile = open(self.input_path, "r")
                col_names = []
                lines = []
                i=0        
                for line in infile:
                    if line != "" :
                        lines.append(line)
                        i += 1
                cols = len(col_names)
                infile.close
                self.data = lines                    
            except (OSError):
                return False 

class Play:
    def __init__(self):
        self.game = App()
        self.ask()

    def ask(self):
        lst = self.game.data
        for i in range(0, len(lst)):
            x = lst[i]
            y = x.split(";")
            q = y[0]
            a = y[1]
            print(q)
            resp = input("Is your answer ready? Please, press x for exit or any other key to see the correct answer...")
            if resp=="x":
                print("GAME OVER")
                break
            print(a)
            if i!=len(lst)-1:
                resp = input("Next question? Press x for exit, or any other key to continue...")                
            else:
                print("This was the last question! Well done!")
            if resp=="x":
                print("GAME OVER")
                break

def main():
    testi = Play()
    
main()
