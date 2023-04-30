#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

import os
import random
from ui.gui import GUI
from ui.gui_input_file_selection import GUI_input_file_selection


class UI:
    def __init__(self, use_default_input=True, output_allowed=False):
        self.default_input=use_default_input
        self.output_allowed = output_allowed
        self.__gu = None

    def show_output(self, output_text=""):
        if self.output_allowed: # == True:
            self.__gu = GUI(use_default_input=False, output_allowed=True)
            self.__gu.show_output(output_text)


    def ask_for_input(self, output_text=""):
        resp=None
        if self.output_allowed: # == True
            self.__gu = GUI(use_default_input=False, output_allowed=True)
            resp = self.__gu.ask_for_input(output_text)
        return resp

    def ask_for_input_file(self):
        if self.output_allowed: # == True:
            self.__gu = GUI_input_file_selection()
            resp = self.__gu.input_file_path
        return resp





if __name__ == "__main__":
    import os
    from ui.ui import GUI
    from ui.ui import GUI_input_file_selection

    main()
