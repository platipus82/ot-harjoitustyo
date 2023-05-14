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
    """Class responsible for maintaining parameters for graphic interface windows."""

    def __init__(self):
        """Class constructor."""
        # self.root = tk.Tk()

        # set window size
        self.width = 400
        self.height = 300
        # self.screen_width = self.root.winfo_screenwidth()
        # self.screen_height = self.root.winfo_screenheight()
        # x = int((self.screen_width - self.width) / 2)
        # y = int((self.screen_height - self.height) / 2)
        # self.root.geometry(f"{self.width}x{self.height}+{x}+{y}")

    # def give_root(self):
        # return self.root
