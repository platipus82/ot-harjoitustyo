#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

#import os
import datetime
from processes.app import App
from processes.database import Database
from ui.ui import UI

#from ui.gui import GUI
#from ui.gui_input_file_selection import GUI_input_file_selection


class Play:
    """Class responsible for initiating the program. """

    def __init__(self, use_default_input=True, output_allowed=False):
        """Class constructor.
        Arguments: 
            use_default_input: 
                - boolean parameter 
                - tells if proceed with default inputs for testing purposes, or not
            output_allowed:  
                - boolean parameter 
                - tells if (graphical) output is allowed or not
        """
        self.__exit = False
        self.start_time = datetime.datetime.now()
        self.end_time=None

        self.game = App(use_default_input=use_default_input, output_allowed=output_allowed)

        self.questions_n_total = len(self.game.data)
        self.questions_n_answered = 0
        self.questions_n_correct = 0

        self.__ui = UI(use_default_input=use_default_input, output_allowed=output_allowed)
        self.db = Database(self.__ui, output_allowed=True)
        self.__exit=self.game.exit
        if not self.__exit: # == False:
            #self.ask()
            self.ask_with_answers()

        if self.__exit == True:
            self.end_time = datetime.datetime.now()
            self.elapsed_time = self.end_time-self.start_time
            self.save_results()
            #self.save_results_to_csv()
            self.db.print_summary()

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

    def save_results_to_csv(self):
        answer = self.__ui.ask_for_text(output_text="Please, type your name")
        usr_name = str(answer).strip()

        #print("User name = " + usr_name)
        #output_file_name = self.__ui.ask_for_text(output_text="Please, type the name for output file")
        infile = self.game.input_file_name

        
        # time
        tstart = str(self.start_time)
        tend = str(self.end_time)
        telaps = self.elapsed_time.seconds
        formatted_time = str(self.elapsed_time)
        formatted_time = formatted_time.replace("-", "")
        formatted_time = formatted_time.replace(" ", "_")
        formatted_time = formatted_time.replace(":", "")
        formatted_time = formatted_time.split(".")[0]
        
        # Output
        output_filename_root = infile.replace(".txt", "")
        output_file_name = usr_name + "_" + output_filename_root + "_" + formatted_time + ".txt"       

        print("Output file name: " + output_file_name)
        output_file_name_full = self.db.db_dir + output_file_name
        print("Full path to output file: " + output_file_name_full)
        
        
       
        # n questions
        qntot = self.questions_n_total 
        qnans = self.questions_n_answered 
        qncor = self.questions_n_correct 
        qpcor = qncor/(qntot/100) #"questions_percent_correct"
       
        colnames = ["user", "deck", "start_time", "end_time","elapsed_time"  "questions_n_total", "questions_n_answered", "questions_n_correct", "questions_percent_correct"]
        answers = [usr_name, infile, tstart, tend, telaps, qntot, qnans, qncor, qpcor]
        
        dat = [colnames, answers]
        self.db.write_file(output_csv_file=output_file_name_full, rows_to_write=dat, mode="w")


    def save_results(self):
        usr_name = self.__ui.ask_for_text(output_text="Please, type your name")
        print("User name = " + usr_name)
        #output_file_name = self.__ui.ask_for_text(output_text="Please, type the name for output file")
        infile = self.game.input_file_name

        # Output
        #cols = [["user", "deck", "start_time", "end_time","elapsed_time"  "questions_n_total", "questions_n_answered", "questions_n_correct", "questions_percent_correct"]]
        # time
        tstart = str(self.start_time)
        tend = str(self.end_time)
        telaps = self.elapsed_time.seconds      
        
        # n questions
        qntot = self.questions_n_total 
        qnans = self.questions_n_answered 
        qncor = self.questions_n_correct 
        qpcor = qncor/(qntot/100) #"questions_percent_correct"
       
        
        dat = [[usr_name, infile, tstart, tend, telaps, qntot, qnans, qncor, qpcor]]
        self.db.write_to_db(output_csv_file="", rows_to_write=dat, mode="a")  

    def ask_with_answers(self):
        lst = self.game.data
        #for i in range(0, len(lst)):
        #    y = lst[i].split(";")
        for i, entry in enumerate(lst):
            y = entry.split(";")
            question = y[0]
            answer = y[1]
            msg_pt1 = "Please, write your answer and press Submit" + "\n"
            msg_pt2 = "Press X to eXit the application" + "\n"
            msg = "Question: " + question + "\n" + msg_pt1 + msg_pt2
            resp = self.__ui.ask_for_text(output_text=msg)

            # removing trailing and leading empty spaces
            answer = str(answer).strip()
            resp = str(resp).strip()

        

                        
            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                self.__exit = True
                return
            else:
                self.questions_n_answered += 1
            
            msg_pt1 = "Question: " + question + "\n" 
            msg_pt2 = "Your answer: " + resp  + "\n"
            if str(resp) == str(answer):
                msg_pt3 = "Your answer is correct" + "\n"
                self.questions_n_correct += 1
            else:
                msg_pt3 = "Your answer is incorrect" + "\n"
            msg_pt4 = "Correct answer: " + answer + "\n"
            msg = msg_pt1 + msg_pt2 + msg_pt3 + msg_pt4
            print(resp)
            print(answer)
            print(len(resp))
            print(len(answer))          

            if i!=len(lst)-1:
                msg = msg + "Next question? "
                resp = self.__ui.ask_for_input(output_text=msg)
            else:
                msg = msg + "This was the last question! Well done!"
                self.__ui.show_output(output_text=msg)

            if resp=="x":
                msg = "GAME OVER"
                self.__ui.show_output(output_text=msg)
                self.__exit = True
                return
        #self.__exit = False
        