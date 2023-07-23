#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

import tkinter as tk
from tkinter import filedialog
import os
from ui.window_parameters import WindowParameters


class FileSelectionView:
    """Class responsible for user interactions via graphical interface during the initiation of the program, and input selection."""

    def __init__(self):
        """
        Class constructor.
        Function will
            - intialize Tkinter and WindowParameter instances   
            - set window size
          -    set text labels
        """
        self.window = WindowParameters()
        self.root = tk.Tk()

        self.width = self.window.width
        self.height = self.window.height
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        x = int((self.screen_width - self.width) / 2)
        y = int((self.screen_height - self.height) / 2)
        self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

        self.root.title("Select a file")
        self.input_path = os.path.join(os.getcwd(), "src", "inputs")
        if not os.path.isfile(self.input_path):
            self.input_file_path = ""

        self.check_that_input_folder_exists()
        self.root.mainloop()

    def check_that_input_folder_exists(self):
        """Function will check that input folder exists and is not empty."""

        if os.path.exists(self.input_path) and os.path.isdir(self.input_path) and os.listdir(self.input_path):
            self.files = os.listdir(self.input_path)
            self.files = [x for x in self.files if x != "__init__.py"]
            self.file_var = tk.StringVar(value=self.files)
            self.file_listbox = tk.Listbox(
                self.root, listvariable=self.file_var)
            scrollbar = tk.Scrollbar(
                self.root, orient=tk.VERTICAL, command=self.file_listbox.yview)
            self.file_listbox.configure(yscrollcommand=scrollbar.set)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
            self.file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            tk.Button(self.root, text="Select",
                      command=self.select_file).pack()
            tk.Button(self.root, text="Choose another file",
                      command=self.choose_file).pack()
        else:
            self.files = []
            self.file_var = tk.StringVar(
                value="No files found in the input folder!")
            tk.Label(self.root, textvariable=self.file_var).pack()
            tk.Button(self.root, text="Choose another file",
                      command=self.choose_file).pack()

    def select_file(self):
        """Function will ask user to choose the correct input file from the list."""
        selected_file = self.file_listbox.get(self.file_listbox.curselection())
        self.input_file_path = os.path.join(self.input_path, selected_file)
        self.file_listbox.pack_forget()
        self.root.destroy()

    def choose_file(self):
        """Function will ask user to choose the correct input file."""
        path = filedialog.askopenfilename()
        if path:
            self.input_file_path = path
            self.file_var.set(self.input_file_path.split("/")[-1])
            self.file_listbox.pack_forget()
            self.root.destroy()

    def choose_directory(self):
        """Function will ask user to choose the alternative directory for input files."""

        path = filedialog.askdirectory()
        if path:
            os.chdir(path)
            pth = os.path.join(os.getcwd(), "src", "inputs")
            self.input_path = pth
            self.setup_file_listbox()
            if not self.files:
                self.file_var = tk.StringVar(
                    value="No files found in the input folder!")
                tk.Label(self.root, textvariable=self.file_var).pack()
