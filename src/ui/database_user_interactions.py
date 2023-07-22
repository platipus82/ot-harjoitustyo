#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 10 July 2023

@author: ok
'''

import os
import csv
import sqlite3


class DatabaseUserInteractions:
    """Class responsible for describing the data for user. """

    def __init__(self, database_interactions):
        """
        Class constructor
        - no input parameters
        - initializes two instance variables:
            self.database_interactions: An instance of DatabaseInteractions.
            self.summary: An empty string that will hold the summary information.
        """
        self.database_interactions = database_interactions
        self.data = self.database_interactions.data
        self.summary = ""

    def give_summary_data(self):
        """Function will return the data from SQL-database"""
        self.data = self.database_interactions.get_sql_db_data()  # Update self.data
        all_results = self.data
        return all_results

    def give_summary(self):
        """Function will return the summary"""
        return self.summary

    def give_summary_of_last_session(self):
        """Function will return the summary of the last session"""
        msg = ""
        last = self.give_summary_data()[-1]
        msg = msg + "Summary of this session:" + "\n"
        cols = self.database_interactions.tell_db_colnames()[0]
        for i, entry in enumerate(last):
            msg = msg + cols[i] + ": " + entry + "\n"
        return msg

    def __describe_n_of_users(self, dat):
        """Function will return the description of n of users"""
        users = []
        for i, entry in enumerate(dat):
            if i != 0:
                user = entry[0]
                users.append(user)
        users = list(set(users))
        msg = str(len(users)) + " different users" + "\n"
        return msg

    def __describe_n_of_input_files(self, dat):
        """Function will return the description of n of input files"""
        infiles = []
        for i, entry in enumerate(dat):
            if i != 0:
                infile = entry[1]
                infiles.append(infile)
        infiles = list(set(infiles))
        msg = str(len(infiles)) + \
            " different decks (input files) have been used" + "\n"
        return msg

    def __describe_total_time(self, dat):
        """Function will return the description of used time"""
        times = []
        for i, entry in enumerate(dat):
            if i != 0:
                used_time = entry[4]
                times.append(int(used_time))
        total_time = sum(times)
        msg = str(total_time) + " seconds has been spent in total"+"\n"
        return msg

    def __total_checked_questions(self, dat):
        """Function will return the description of total checked questions"""
        questions = []
        for i, entry in enumerate(dat):
            if i != 0:
                nquest = entry[6]
                questions.append(int(nquest))
        msg = str(sum(questions)) + \
            " questions have been viewed in total"+"\n"
        return msg

    def __total_answered_questions(self, dat):
        """Function will return the description of total answered questions"""
        questions = []
        for i, entry in enumerate(dat):
            if i != 0:
                nquest = entry[7]
                questions.append(int(nquest))
        msg = str(sum(questions)) + \
            " questions have been answered in total"+"\n"
        return msg

    def __correctly_answered_questions(self, dat):
        """Function will return the description of correctly answered questions"""
        questions = []
        for i, entry in enumerate(dat):
            if i != 0:
                nquest = entry[8]
                questions.append(int(nquest))
        msg = str(sum(questions)) + \
            " questions have been answered correctly"+"\n"
        return msg

    def __percentage_of_correct(self, dat):
        """Function will return the description of percentage of questions answered correctly"""
        results = []
        for i, entry in enumerate(dat):
            if i != 0:
                x = entry[9]
                results.append(float(x))
        msg = str(sum(results)/len(results)) + \
            " was the average percent of correct answers"+"\n"
        return msg

    def give_summary_of_db(self):
        """Function will return the description of the database"""
        dat = self.data
        msg = "Currently database contains: " + "\n"
        msg = msg + str(len(dat)) + " recorded sessions" + "\n" + \
            self.__describe_n_of_users(dat) + \
            self.__describe_n_of_input_files(dat) + \
            self.__describe_total_time(dat) + \
            self.__total_checked_questions(dat) + \
            self.__total_answered_questions(dat) + \
            self.__correctly_answered_questions(dat) + \
            self.__percentage_of_correct(dat)
        return msg

    def make_summary(self):
        """Function creating the summary of last session and database."""
        last_session = self.give_summary_of_last_session()
        whole_database = self.give_summary_of_db()
        msg = last_session + whole_database
        self.summary = msg
