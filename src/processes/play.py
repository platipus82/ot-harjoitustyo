#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 12 May 2023

@author: ok
'''

# import os
import datetime
from processes.app import App
from processes.database import Database
from ui.ui import UI

# from ui.gui import GUI
# from ui.gui_input_file_selection import GUI_input_file_selection


class Play:
    def __init__(self, use_default_input=True, output_allowed=False):
        self.use_default_input = use_default_input
        self.output_allowed = output_allowed
        self.start_time = datetime.datetime.now()
        self.end_time = ""
        self.mode = None
        self.__exit = False
        self.game = App(use_default_input=use_default_input,
                        output_allowed=output_allowed)
        self.questions_n_total = len(self.game.data)
        self.questions_n_checked = 0
        self.questions_n_answered = 0
        self.questions_n_correct = 0

        self.__ui = UI(use_default_input=use_default_input,
                       output_allowed=output_allowed)
        self.set_mode()

        self.db = Database(output_allowed=output_allowed)
        self.__exit = self.game.exit
        if self.__exit == False and self.output_allowed == True:
            self.ask()
            # self.ask_with_answers()

        # print("questions over, saving results")
        if self.mode == 0:
            self.__exit = True
        # self.save_results2()
        if self.__exit == True:
            self.end_time = datetime.datetime.now()
            self.elapsed_time = self.end_time-self.start_time
            self.save_results()
            # self.save_results_to_csv()
            # self.db.print_summary()
            if self.output_allowed:
                msg = self.db.give_summary()
                self.__ui.show_output(output_text=msg)

    def set_mode(self):
        if self.use_default_input == False and self.output_allowed == True:
            resp = self.__ui.set_mode()
            if resp == "x":
                self.__exit = True
            else:
                self.mode = resp
        else:
            self.mode = 0

    def ask(self):
        lst = self.game.data
        while not self.__exit:
            for i, entry in enumerate(lst):
                y = entry.split(";")
                question = y[0]
                answer = y[1]
                if i != len(lst)-1:
                    last_question = False
                else:
                    last_question = True
                self.questions_n_checked += 1
                if self.output_allowed == True:
                    resp = self.__ui.ask(
                        question=question, answer=answer, last_question=last_question)
                    self.__exit = self.__ui.exit
                    if self.__ui.last_question_correct == True:
                        self.questions_n_correct += 1
                    self.questions_n_answered += 1
                    if self.__exit:
                        break
            self.__exit = True

    '''def save_results_to_csv(self):
        answer = self.__ui.ask_for_text(output_text="Please, type your name")
        usr_name = str(answer).strip()
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
        output_file_name_full = self.db.db_dir + output_file_name       
        
       
        # n questions
        qntot = self.questions_n_total 
        qnchecked = self.questions_n_checked 
        qnans = self.questions_n_answered 
        qncor = self.questions_n_correct 
        qpcor = qncor/(qntot/100) #"questions_percent_correct"
       
        colnames = ["user", "deck", "start_time", "end_time","elapsed_time",  "questions_n_total","questions_n_visited", "questions_n_answered", "questions_n_correct", "questions_percent_correct"]
        answers = [usr_name, infile, tstart, tend, telaps, qntot, qnchecked, qnans, qncor, qpcor]
        
        dat = [colnames, answers]
        self.db.write_file(output_csv_file=output_file_name_full, rows_to_write=dat, mode="w")
        '''

    def save_results(self):
        usr_name = self.__ui.ask_for_text(output_text="Please, type your name")
        infile = self.game.input_file_name

        # Output
        # cols = [["user", "deck", "start_time", "end_time","elapsed_time"  "questions_n_total", "questions_n_answered", "questions_n_correct", "questions_percent_correct"]]
        # time
        tstart = str(self.start_time)
        tend = str(self.end_time)
        telaps = self.elapsed_time.seconds

        # n questions
        qntot = self.questions_n_total
        qnche = self.questions_n_checked
        qnans = self.questions_n_answered
        qncor = self.questions_n_correct
        qpcor = qncor/(qntot/100)  # "questions_percent_correct"

        dat = [[usr_name, infile, tstart, tend,
                telaps, qntot, qnche, qnans, qncor, qpcor]]
        if self.output_allowed:
            self.db.write_to_db(output_csv_file="",
                                rows_to_write=dat, mode="a")
            self.db.write_to_sql_db(rows_to_write=dat)
