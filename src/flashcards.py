# -*- coding: utf-8 -*-
'''
Created on 3 Apr 2023

@author: olegk
'''
import pygame
import random
import math
import time

import sys
import os

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



def read_input_file(file_name):        
    try:
        infile = open(file_name, "r")
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
   #    print("There are ", cols, " cols")        
        infile.close
        return(lines)
            
    except (OSError):
        return False 
    
def ask(lst):
    #print(lst)
    for x in lst:
        #print(x)
        y = x.split(";")
        #print(y)
        q = y[0]
        a = y[1]
        #print(q)
        print(q)
        resp = input("Is your answer ready? Please, press any key to see the correct answer...")
        print(a)
        resp = input("Next question? Press any key to continue...")
        
          
def read():
    while True:
        num = input("Give a number: ")
        try:
            num = int(num)
            if 5 <= num <= 10:
                break
            else:
                print("You must choose an integer between 5 and 10")

        except:
            print("The number must be an integer between 5 and 10")
    print(f"You chose number: {num}")
    
    
class App:
    def __init__(self):
        pygame.init()
        random.seed(a=None, version=2)
        
        # Dimensions
        self.height = 480 #len(self.map)
        self.width = 640 #len(self.map[0])

        # Pisteet
        self._points = 0
        self._lvlpoints = 0
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode((640, 480))

        self._end = False
        pygame.display.set_caption("Flashcards")
        self.loop()
        
    def draw_display(self):
        self.display.fill((0, 0, 0))
        #if self._lvl <=5:   self.display.fill((0, 0, 0))
        #else: self.display.fill((250, 0, 0))
            
        pygame.display.flip()
        
    def loop(self):
        while True:
            self.draw_display()

def play():
    App()
    

def main():
    #App()
    print(os.getcwd())
    #inp = read_input_file("\src\inputs\Topic1.txt")
    inppth = os.getcwd() + "/src/inputs/Topic1.txt"
    inp = read_input_file(inppth)
    #print("Input: ")
    #print(inp)
    ask(inp)
    
    pass

main()
#if __name__ == "__main__":
#    main()

