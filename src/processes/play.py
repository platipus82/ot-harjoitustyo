#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 12 May 2023

@author: ok
'''

import datetime
from processes.app import App
from repositories.database import Database
from ui.user_interface import UserInterface


class Play:
    """Class responsible for initiating the program and process logic. """

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
        self.use_default_input = use_default_input
        self.output_allowed = output_allowed
        self.start_time = datetime.datetime.now().replace(microsecond=0)
        self.end_time = ""
        self.mode = None
        self.__exit = False
        self.game = App(use_default_input=use_default_input,
                        output_allowed=output_allowed)
        self.questions_n_total = len(self.game.data)
        self.questions_n_checked = 0
        self.questions_n_answered = 0
        self.questions_n_correct = 0

        self.__ui = UserInterface(use_default_input=use_default_input,
                                  output_allowed=output_allowed)
        self.set_mode()

        self.database = Database(output_allowed=output_allowed)
        self.__exit = self.game.exit
        if self.output_allowed and not self.__exit:
            self.ask()

        if self.mode == 0:
            self.__exit = True
        if self.__exit:
            self.end_time = datetime.datetime.now().replace(microsecond=0)
            self.elapsed_time = self.end_time-self.start_time
            self.save_results()
            self.database.data = self.database.database_interactions.data[:]
            self.database.database_user_interactions.make_summary()
            if self.output_allowed:
                msg = self.database.database_user_interactions.give_summary()
                self.__ui.show_output(output_text=msg)

    def set_mode(self):
        """Function setting the game mode based on response from MainView"""
        if self.output_allowed and not self.use_default_input:
            resp = self.__ui.set_mode()
            if resp == "x":
                self.__exit = True
            else:
                self.mode = resp
        else:
            self.mode = 0

    def update_question_counters(self):
        """Function responsible for updating question counters. """
        if self.__ui.last_question_correct:
            self.questions_n_correct += 1
        self.questions_n_answered += 1

    def ask(self):
        """Function looping over questions and asking them."""
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
                if self.output_allowed:
                    self.__ui.ask(
                        question=question, answer=answer, last_question=last_question)
                    self.__exit = self.__ui.exit
                    self.update_question_counters()
                if self.__exit:
                    break

            self.__exit = True

    def save_results(self):
        """Function responsible for saving the results in the end of the game. """
        usr_name = self.__ui.ask_for_text(output_text="Please, type your name")
        infile = self.game.input_file_name

        # time
        tstart = str(self.start_time)
        tend = str(self.end_time)
        telaps = self.elapsed_time.seconds

        # n questions
        qntot = self.questions_n_total
        qnche = self.questions_n_checked
        qnans = self.questions_n_answered
        qncor = self.questions_n_correct
        qpcor = qncor/(qntot/100)

        dat = [[usr_name, infile, tstart, tend,
                telaps, qntot, qnche, qnans, qncor, qpcor]]
        if self.output_allowed:
            self.database.database_file_handling.write_to_db(output_csv_file=self.database.db_path,
                                                             rows_to_write=dat, mode="a")
            self.database.database_file_handling.write_to_sql_db(
                rows_to_write=dat)
        return dat
