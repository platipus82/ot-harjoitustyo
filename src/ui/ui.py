#!/usr/bin/python  
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

import tkinter as tk
from tkinter import filedialog
import os



class Window_parameters:
    def __init__(self):
        #self.root = tk.Tk()

        # set window size
        self.width = 400
        self.height = 300
        #self.screen_width = self.root.winfo_screenwidth()
        #self.screen_height = self.root.winfo_screenheight()
        #x = int((self.screen_width - self.width) / 2)
        #y = int((self.screen_height - self.height) / 2)
        #self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        
    #def give_root(self):
        #return self.root

class GUI_input_file_selection:
    def __init__(self):
        self.window = Window_parameters()
        self.root = tk.Tk()
        #self.root = self.window.root()
        
        # set window size
        self.width = self.window.width
        self.height = self.window.height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        x = int((self.screen_width - self.width) / 2)
        y = int((self.screen_height - self.height) / 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")
        
        
        # texts
        self.root.title("Select a file")
        self.input_path = os.getcwd() + "\src\inputs\\"
        if not os.path.isfile(self.input_path):
            self.input_path = os.getcwd() + "/src/inputs/"
            self.input_file_path = ""

        # check if the input folder exists and has files
        if os.path.exists(self.input_path) and os.path.isdir(self.input_path) and os.listdir(self.input_path):
            self.files = os.listdir(self.input_path)
            self.files = [x for x in self.files if x != "__init__.py"]
            #self.file_var = tk.StringVar(value=self.files[0])
            self.file_var = tk.StringVar(value=self.files)
            self.file_listbox = tk.Listbox(self.root, listvariable=self.file_var)
            scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.file_listbox.yview)
            self.file_listbox.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            #self.file_listbox.pack()
            tk.Button(self.root, text="Select", command=self.select_file).pack()
            tk.Button(self.root, text="Choose another file", command=self.choose_file).pack()
        else:
            self.files = []
            self.file_var = tk.StringVar(value="No files found in the input folder!")
            tk.Label(self.root, textvariable=self.file_var).pack()
            tk.Button(self.root, text="Choose another file", command=self.choose_file).pack()

        self.root.mainloop()

    def select_file(self):
        selected_file = self.file_listbox.get(self.file_listbox.curselection())
        self.input_file_path = os.path.join(self.input_path, selected_file)
        self.file_listbox.pack_forget()
        self.root.destroy()

    def choose_file(self):
        path = filedialog.askopenfilename()
        if path:
            self.input_file_path = path
            self.file_var.set(self.input_file_path.split("/")[-1])
            self.file_listbox.pack_forget()
            self.root.destroy()

    def choose_directory(self):
        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            pth = os.getcwd() + "\src\inputs\\"
            if not os.path.isfile(pth):
                pth = os.getcwd() + "/src/inputs/"
            self.input_path = pth
            self.setup_file_listbox()
            if not self.files:
                self.file_var = tk.StringVar(value="No files found in the input folder!")
                tk.Label(self.root, textvariable=self.file_var).pack()

class GUI:
    def __init__(self, use_default_input=True, output_allowed=False):
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
        #print("GUI.show_output")

        if self.output_allowed == True: 
            output_label = tk.Label(self.root, text=output_text).pack()
            self.root.wait_window()

    
    def ask_for_input(self, output_text):
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
        pth = GUI_input_file_selection()
        return pth
    
    def set_result(self, result, window):
        self.result = result
        window.destroy()
        
class UI:
    def __init__(self, use_default_input=True, output_allowed=False):
        self.default_input=use_default_input
        self.output_allowed = output_allowed
        
    def show_output(self, output_text=""):
        #print("UI.show_output")
        if self.output_allowed == True: 
            #print(output_text)
            gu = GUI(use_default_input=False, output_allowed=True)
            #response = gu.show_output(x)
            gu.show_output(output_text)
            #print(response)
        
            
    def ask_for_input(self, output_text=""):
        #print("UI.ask_for_input")

        resp=None
        if self.output_allowed == True: 
            #resp = input(output_text)
            gu = GUI(use_default_input=False, output_allowed=True)
            resp = gu.ask_for_input(output_text)
        return resp

    def ask_for_input_file(self, output_text=""):
        #print("UI.ask_for_input_file")
        if self.output_allowed == True: 
            gu = GUI_input_file_selection()
            resp = gu.input_file_path
        return resp       
    

