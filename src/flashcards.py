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
        tiedosto = open(file_name, "r")
        sarake_otsikot = []
        rivit = []
        i=0        
        for rivi in tiedosto:
            #while rivi != "" :          # jokaisella rivilla joka ei ole tyhja...
            if rivi != "" :
                #print(rivi)
                rivit.append(rivi)
                #while i==0:
                #rivi = rivi.rstrip('\n')    # poista rivilta newline merkki
                #alkiot = rivi.split('\t')
                #for alkio in alkiot:
                    #if alkio != "" :
                        #sarake_otsikot.append(alkio)
                i += 1
        #print(sarake_otsikot)
        sarakkeita = len(sarake_otsikot)
   #    print("sarakkeita on", sarakkeita)        
        tiedosto.close
        return(rivit)
            
    except (OSError):
        return False 
    
def kysele(lst):
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
        
          
def lue():
    while True:
        luku = input("syötä luku: ")
        try:
            luku = int(luku)
            if 5 <= luku <= 10:
                break
            else:
                print("Syötteen on oltava kokonaisluku väliltä 5...10")

        except:
            print("Syötteen on oltava kokonaisluku väliltä 5...10")
    print(f"syötit luvun: {luku}")
    
    
class App:
    def __init__(self):
        pygame.init()
        random.seed(a=None, version=2)
        
        # Mitat
        self.korkeus = 480 #len(self.kartta)
        self.leveys = 640 #len(self.kartta[0])

        # Pisteet
        self._pisteet = 0
        self._tasopisteet = 0
        self.kello = pygame.time.Clock()
        self.naytto = pygame.display.set_mode((640, 480))

        self._loppu = False
        pygame.display.set_caption("Flashcards")
        self.silmukka()
        
    def piirra_naytto(self):
        self.naytto.fill((0, 0, 0))
        #if self._taso <=5:   self.naytto.fill((0, 0, 0))
        #else: self.naytto.fill((250, 0, 0))
            
        pygame.display.flip()
        
    def silmukka(self):
        while True:
            self.piirra_naytto()

def pelaa():
    App()
    

def main():
    #App()
    print(os.getcwd())
    #inp = read_input_file("\src\inputs\Topic1.txt")
    inppth = os.getcwd() + "/src/inputs/Topic1.txt"
    inp = read_input_file(inppth)
    #print("Input: ")
    #print(inp)
    kysele(inp)
    
    pass

main()
#if __name__ == "__main__":
#    main()
