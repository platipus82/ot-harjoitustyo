# -*- coding: utf-8 -*-
'''
Created on 10 Apr 2023

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
        #self.input_dir = os.getcwd() + "\src\inputs\\"
        self.input_dir = os.getcwd() + "\inputs\\"

    def set_input_path(self):
        #self.input_path = os.getcwd() + "\src\inputs\\"
        self.input_path = os.getcwd() + "\inputs\\"
        filelist = os.listdir(self.input_dir)
        filelist_description = "Currently available files are: "
        for i in range(0, len(filelist)):
            filepart =  str(i) + ": " + filelist[i]
            filelist_description = filelist_description+filepart
        #print(filelist_description)
        filelist_description = filelist_description + ". Please, chose correct input file by typing the corresponding number..."

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
        print(f"You´ve chosen file {filelist[num]} ({num})") 
        self.input_path = self.input_dir + "/" + filelist[num]

    def get_input_data(self): 
            try:
                infile = open(self.input_path, "r")
                col_names = []
                lines = []
                i=0        
                for line in infile:
                    #while rivi != "" :          # jokaisella rivilla joka ei ole tyhja...
                    if line != "" :
                        #print(rivi)
                        lines.append(line)
                        #while i==0:
                        #line = line.rstrip('\n')    # poista rivilta newline merkki
                        #items = line.split('\t')
                        #for item in items:
                            #if items != "" :
                                #col_names.append(item)
                        i += 1
                #print(col_names)
                cols = len(col_names)
                #print("There are ", cols, " cols")        
                infile.close
                self.data = lines 
                    
            except (OSError):
                return False 

class Play:
    def __init__(self):
        self.game = App()
        self.ask()

    def ask(self):
        #print(lst)
        lst = self.game.data
        for i in range(0, len(lst)):
            #print(i)
            x = lst[i]
            y = x.split(";")
            #print(x)
            #print(y)
            q = y[0]
            a = y[1]
            #print(q)
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
    