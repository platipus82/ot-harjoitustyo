#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

#import os
from processes.app import App
from ui.ui import UI
#from ui.gui import GUI
#from ui.gui_input_file_selection import GUI_input_file_selection


class Play:
    """Class responsible for initiating the program. """

    def __init__(self, use_default_input=True, output_allowed=False):
        """Class constructor.
        Arguments: 
            use_default_input: boolean parameter telling whether we want to proceed with default inputs for testing purposes, or not
            output_allowed:  boolean parameter telling whether (graphical) output is allowed or should be omitted
        """
        self.__exit = False
        self.game = App(use_default_input=use_default_input, output_allowed=output_allowed)
        self.__ui = UI(use_default_input=use_default_input, output_allowed=output_allowed)
        self.__exit=self.game.exit
        if not self.__exit: # == False:
            self.ask()

    def ask(self):
        """Function looping over questions and asking them."""

        lst = self.game.data
        for i, entry in enumerate(lst):
            y = entry.split(";")
            question = y[0]
            answer = y[1]
            msg_pt1 = "Please, press proceed to see the correct answer" + "\n"
            msg_pt2 = "Press exit to exit the application" + "\n"
            msg = "Question: " + question + "\n" + msg_pt1 + msg_pt2
            resp = self.__ui.ask_for_input(output_text=msg)

            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                break
            msg = "Question: " + question + "\n" + "Answer: " + "\n" + answer + "\n"

            if i!=len(lst)-1:
                msg = msg + "Next question? "
                resp = self.__ui.ask_for_input(output_text=msg)
            else:
                msg = msg + "This was the last question! Well done!"
                self.__ui.show_output(output_text=msg)

            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                break
