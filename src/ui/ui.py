#!/usr/bin/python  
# -*- coding: utf-8 -*-

'''
Created on 17 Apr 2023

@author: ok
'''

class UI:
    def __init__(self, use_default_input=True, output_allowed=False):
        self.default_input=use_default_input
        self.output_allowed = output_allowed
        
    def show_output(self, output_text=""):
        if self.output_allowed == True: 
            print(output_text)
            
    def ask_for_input(self, output_text=""):
        if self.output_allowed == True: 
            resp = input(output_text)
        return resp