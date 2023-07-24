#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

import tkinter as tk
from tkinter import filedialog


class WindowParameters:
    """Class responsible for maintaining parameters for graphic interface windows."""

    def __init__(self):
        """Class constructor."""
        self.width = 500
        self.height = 400
