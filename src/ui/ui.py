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
    """Class responsible for user interactions. If I/O is allowed, it will activate GUI-class responsible for GUI"""

    def __init__(self, use_default_input=True, output_allowed=False):
        """Class constructor.
        Arguments: 
            use_default_input: boolean parameter telling whether we want to proceed with default inputs for testing purposes, or not
            output_allowed:  boolean parameter telling whether (graphical) output is allowed or should be omitted
        """
        self.default_input=use_default_input
        self.output_allowed = output_allowed
        self.__gu = None

    def show_output(self, output_text=""):
        """Function will ask GUI to show the output - if output is allowed. 
        Arguments:
            output_text: output text
        """
        if self.output_allowed: # == True:
            self.__gu = GUI(use_default_input=False, output_allowed=True)
            self.__gu.show_output(output_text)


    def ask_for_input(self, output_text=""):
        """Function which will ask GUI to ask for user input. Function will receive user input from GUI and send it back for processing to the calling function.
        Arguments:
            output_text: text which will be showed to the user
        """
        resp=None
        if self.output_allowed: # == True
            self.__gu = GUI(use_default_input=False, output_allowed=True)
            resp = self.__gu.ask_for_input(output_text)
        return resp

    def ask_for_input_file(self):
        """Function will GUI to ask user to choose the correct input file. Selected file will be sent back for processing to the calling function.""" 

        if self.output_allowed: # == True:
            self.__gu = GUI_input_file_selection()
            resp = self.__gu.input_file_path
        return resp

    def ask_for_text(self, output_text=""):
        #print("UI.ask_for_input")

        resp=None
        if self.output_allowed == True: 
            #resp = input(output_text)
            gu = GUI(use_default_input=False, output_allowed=True)
            resp = gu.ask_for_text(output_text)
        return resp

if __name__ == "__main__":
    import os
    from ui.ui import GUI
    from ui.ui import GUI_input_file_selection

    main()
