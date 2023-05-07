#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

import os
import random
from ui.ui import UI
#from ui.gui import GUI
#from ui.gui_input_file_selection import GUI_input_file_selection

class App:
    """Class responsible for running the program. """

    def __init__(self, use_default_input=True, output_allowed=False):
        """Class constructor.
        Arguments: 
            use_default_input: boolean. Proceed with default inputs for testing purposes, or not
            output_allowed:  boolean. Is (graphical) output allowed or not
        """

        self.default_input=use_default_input
        self.output_allowed=output_allowed
        self.input_dir = ""
        self.input_path = ""
        if not self.default_input:
            self.__ui = UI(use_default_input=self.default_input, output_allowed=output_allowed)
        self.exit = False
        self.data = []
        self.filelist = []
        self.set_parameters()
        self.input_file_name = self.give_input_filename()
        self.shuffle_questions()

    def give_input_filename(self):
        x = self.input_path
        x = x.replace("\\", ";")
        x = x.replace("/", ";")
        x = x.split(";")[-1]
        return x

    def set_parameters(self):
        """Parameter setter allowing input choice based on arguments received by constructor."""
        self.set_input_dir()
        self.get_input_filelist()

        if self.default_input: # ==True
            self.set_input_path_default()
        else:
            self.set_input_path()
        self.get_input_data()

    def set_input_dir(self):
        """Function setting input directory."""
        self.input_dir = os.getcwd() + "\inputs\\"
        if not os.path.isdir(self.input_dir):
            self.input_dir = os.getcwd() + "/src/inputs//"


    def get_input_filelist(self):
        """Function getting input file list."""
        filelist = os.listdir(self.input_dir)
        filelist = [x for x in filelist if x.endswith(".csv") or x.endswith(".txt") ]
        self.filelist = filelist

    def set_input_path_default(self):
        """Function setting default directory as input directory ."""
        filelist = self.filelist
        filelist_description = "Currently available files are: " + "\n"
        for i, filename in enumerate(filelist):
            filepart =  str(i) + ": " + filename + "\n"
            filelist_description = filelist_description+filepart


        new_part = "Currently running in default input mode and will use the first available file."
        filelist_description = filelist_description + new_part
        self.input_path = self.input_dir + "/" + self.filelist[0]
        if not os.path.isfile(self.input_path):
            self.input_path = self.input_dir + "\\" + self.filelist[0]
        filelist_description = filelist_description + self.filelist[0]
        if not self.default_input:
            resp = self.__ui.ask_for_input(output_text=filelist_description)
            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                self.exit = True
                return

    def set_input_path(self):
        """Function setting the path for input file"""
        pth= self.__ui.ask_for_input_file() #GUI_input_file_selection()
        self.input_path = pth


    def get_input_data(self):
        """Function reading in the input datafile"""
        try:
            with open(self.input_path, "r", encoding="utf-8") as infile:
                lines = []
                i=0
                for line in infile:
                    if line != "" :
                        lines.append(line)
                        i += 1
                self.data = lines
                return True
        except OSError:
            return False

    def shuffle_questions(self):
        """Function shuffling the questions into random order."""
        lst = self.data
        random.shuffle(lst)
        self.data=lst






#if __name__ == "__main__":
#    import os
#    from ui.ui import GUI
#    from ui.ui import GUI_input_file_selection

#    main()
