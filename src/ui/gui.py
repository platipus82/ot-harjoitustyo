#!/usr/bin/python  
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

import tkinter as tk
from tkinter import filedialog
import os
from ui.window_parameters import Window_parameters

class GUI:
    """Class responsible for user interactions via graphical interface during the execution of the program """
    
    def __init__(self, use_default_input=True, output_allowed=False):
        """Class constructor.
        Arguments: 
            use_default_input: boolean parameter telling whether we want to proceed with default inputs for testing purposes, or not
            output_allowed:  boolean parameter telling whether (graphical) output is allowed or should be omitted
        """
        
        self.root = tk.Tk()
        self.default_input=use_default_input
        self.output_allowed = output_allowed
        
        # set window size
        self.window = Window_parameters()
        self.width = self.window.width
        self.height = self.window.height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        x = int((self.screen_width - self.width) / 2)
        y = int((self.screen_height - self.height) / 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
    
    def show_output(self, output_text=""):
        """Function which will show the textual output via tkinter window
        Arguments:
            output_text: output text
        """
        #print("GUI.show_output")

        if self.output_allowed == True: 
            output_label = tk.Label(self.root, text=output_text).pack()
            self.root.wait_window()

    
    def ask_for_input(self, output_text):
        """Function which will show user the text asking for user input. User input will be sent back for processing to the calling function.
        Arguments:
            output_text: text which will be showed to the user
        """
        #print("GUI.ask_for_input")

        #root = tk.Tk()
        self.root.title("Input")
        input_label = tk.Label(self.root, text=output_text)
        input_label.pack()
        proceed_button = tk.Button(self.root, text="Proceed", command=lambda: self.set_result("y", self.root))
        proceed_button.pack(side="left")
        exit_button = tk.Button(self.root, text="Exit", command=lambda: self.set_result("x", self.root))
        exit_button.pack(side="right")
        self.root.wait_window()
    
        return self.result
    
    def ask_for_file(self):
        """Function will ask GU-interface to ask user to choose the correct input file.""" 
        pth = GUI_input_file_selection()
        return pth
    
    def ask_for_text(self, output_text):
        # Create text input window with same dimensions and position as ask_for_input
        self.root.title("Input")
        input_label = tk.Label(self.root, text=output_text)
        input_label.pack()
        input_entry = tk.Entry(self.root)
        input_entry.pack()
        proceed_button = tk.Button(self.root, text="Proceed", command=lambda: self.set_text_result(input_entry.get(), self.root))
        proceed_button.pack(side="left")
        exit_button = tk.Button(self.root, text="Exit", command=lambda: self.set_text_result(None, self.root))
        exit_button.pack(side="right")
        self.root.wait_window()
        return self.result

    def set_result(self, result, window):
        self.result = result
        window.destroy()

    def set_text_result(self, result, window):
        self.result = result 
        window.destroy()

