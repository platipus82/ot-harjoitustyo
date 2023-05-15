#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 May 2023

@author: ok
'''

import os
import csv
import sqlite3


class Database:
    def __init__(self, output_allowed=True):
        # print("Class Database")
        # self.db_dir = os.getcwd() + "\src\repositories\\"
        # if not os.path.isfile(self.db_dir):
        #    self.db_dir = os.getcwd() + "/src/repositories/"
        self.db_dir = os.path.join(os.getcwd(), "src", "repositories")
        # print(self.db_dir)
        self.output_allowed = output_allowed

        # .csv database
        # self.db_path = self.db_dir + "csv_database.csv"
        self.db_path = os.path.join(self.db_dir, "csv_database.csv")
        self.data = []
        if not os.path.isfile(self.db_path):
            self.make_new_db_file()
        # print(self.db_dir)
        # print(self.db_path)

        # SQL-database
        # self.sql_db_path = self.db_dir + "database.db"
        self.sql_db_path = os.path.join(self.db_dir, "database.db")
        if not os.path.isfile(self.sql_db_path):
            self.make_new_sql_db_file()

        # Summary
        self.summary = ""
        self.make_summary()

    def make_summary(self):
        # results = self.give_summary_data()
        self.give_summary_data()
        last_session = self.give_summary_of_last_session()
        whole_database = self.give_summary_of_db()
        msg = last_session + whole_database
        self.summary = msg

    def make_new_sql_db_file(self):
        database = sqlite3.connect(self.sql_db_path)
        database.isolation_level = None
        cursor = database.cursor()

        # Step 1: creating an empty table
        # print("...1: Creating an empty table if one does not exist yet.")
        part1 = "CREATE TABLE IF NOT EXISTS Records "
        part2 = "(id TEXT NOT NULL, user TEXT NOT NULL, deck TEXT NOT NULL, "
        part3 = "start_time TEXT NOT NULL, end_time TEXT NOT NULL, "
        part4 = "elapsed_time TEXT NOT NULL, questions_n_total INTEGER, "
        part5 = "questions_n_checked INTEGER, questions_n_answered INTEGER, "
        part6 = "questions_n_correct INTEGER, questions_percent_correct REAL);"
        whole_command = part1+part2+part3+part4+part5+part6
        cursor.execute(whole_command)

    def make_db_dir(self):
        # check if the input folder exists and has files
        if os.path.exists(self.db_dir) and os.path.isdir(self.db_dir):
            pass
        else:
            os.mkdir(self.db_dir)

    def tell_db_colnames(self):
        cols = ["user", "deck", "start_time", "end_time",
                "elapsed_time", "questions_n_total"]
        cols = cols + ["questions_n_checked", "questions_n_answered",
                       "questions_n_correct", "questions_percent_correct"]
        cols = [cols]
        return cols

    def make_new_db_file(self):
        self.write_file(output_csv_file=self.db_path,
                        rows_to_write=self.tell_db_colnames(), mode="w")

    def write_to_db(self, output_csv_file="", rows_to_write=None, mode="a"):
        self.write_file(output_csv_file=output_csv_file,
                        rows_to_write=rows_to_write, mode=mode)  # mode="a"

    def write_to_sql_db(self, rows_to_write=None):
        data = []
        for x in rows_to_write:
            primary_key = x[2]
            x = [primary_key] + x
            data.append(x)

        # for x in data:
        #    print(x)
        database = sqlite3.connect(self.sql_db_path)
        database.isolation_level = None
        cursor = database.cursor()

        cursor.execute("BEGIN")

        # id, user, deck, start_time, end_time, elapsed_time, questions_n_total,
        # questions_n_answered, questions_n_correct, questions_percent_correct
        whole_command = "CREATE TABLE IF NOT EXISTS Records (id STRING PRIMARY KEY, " + \
            "start_time TEXT NOT NULL, end_time TEXT NOT NULL, elapsed_time TEXT NOT NULL, " + \
            "questions_n_total INTEGER, questions_n_checked INTEGER, " + \
            "questions_n_answered INTEGER, " + \
            "questions_n_correct INTEGER, " + \
            "questions_percent_correct REAL);"
        cursor.execute(whole_command)

        whole_command = "INSERT INTO Records (" +\
            "id, user, deck, start_time, end_time, elapsed_time, questions_n_total," +\
            "questions_n_checked, questions_n_answered, questions_n_correct, " +\
            "questions_percent_correct )" +\
            "VALUES (?,?,?,?,?,?,?,?,?,?,?);"
        cursor.executemany(whole_command, data)
        cursor.execute("COMMIT")

    def write_file(self, output_csv_file="", rows_to_write=None, mode="a"):
        try:
            with open(output_csv_file, mode, newline='', encoding="utf-8") as myfile:
                filewriter = csv.writer(
                    myfile, quoting=csv.QUOTE_NONE, delimiter=";")
                for row in rows_to_write:
                    filewriter.writerow(row)
            return True
        except OSError:
            return False

    def get_db_data(self):
        try:
            with open(self.db_path, "r", encoding="utf-8") as infile:
                lines = []
                i = 0
                for line in infile:
                    if line != "":
                        items = line.split(";")
                        lines.append(items)
                        i += 1
                self.data = lines
                return True
        except OSError:
            self.data = None
            return False

    def get_sql_db_data(self):
        database = sqlite3.connect(self.sql_db_path)
        database.isolation_level = None
        cursor = database.cursor()
        cursor.execute("BEGIN")
        data = cursor.execute("SELECT * FROM Records;").fetchall()
        database.close()
        listat = []
        for x in data:
            lista = []
            for y in x:
                lista.append(str(y))
            lista.pop(0)
            listat.append(lista)
        self.data = listat

    def give_summary_data(self):
        self.get_sql_db_data()
        all_results = self.data
        return all_results

    def give_summary(self):
        return self.summary

    def give_summary_of_last_session(self):
        msg = ""
        # print(self.data)
        last = self.data[-1]
        msg = msg + "Summary of this session:" + "\n"
        cols = self.tell_db_colnames()[0]
        for i, entry in enumerate(last):
            # print(cols[i] + ": " + entry)
            msg = msg + cols[i] + ": " + entry + "\n"
        return msg

    def __describe_n_of_users(self, dat):
        # n of users
        users = []
        for i, entry in enumerate(dat):
            if i != 0:
                user = entry[0]
                users.append(user)
        users = list(set(users))
        msg = str(len(users)) + " different users" + "\n"
        return msg

    def __describe_n_of_input_files(self, dat):
        # n of input files
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
        # total time
        times = []
        for i, entry in enumerate(dat):
            if i != 0:
                used_time = entry[4]
                times.append(int(used_time))
        total_time = sum(times)
        msg = str(total_time) + " seconds has been spent in total"+"\n"
        return msg

    def __total_checked_questions(self, dat):
        # total checked questions
        questions = []
        for i, entry in enumerate(dat):
            if i != 0:
                nquest = entry[6]
                questions.append(int(nquest))
        msg = str(sum(questions)) + \
            " questions have been viewed in total"+"\n"
        return msg

    def __total_answered_questions(self, dat):
        # total answered questions
        questions = []
        for i, entry in enumerate(dat):
            if i != 0:
                nquest = entry[7]
                questions.append(int(nquest))
        msg = str(sum(questions)) + \
            " questions have been answered in total"+"\n"
        return msg

    def __correctly_answered_questions(self, dat):
        # correctly answered questions
        questions = []
        for i, entry in enumerate(dat):
            if i != 0:
                nquest = entry[8]
                questions.append(int(nquest))
        msg = str(sum(questions)) + \
            " questions have been answered correctly"+"\n"
        return msg

    def __percentage_of_correct(self, dat):
        # percentage of correct
        results = []
        for i, entry in enumerate(dat):
            if i != 0:
                x = entry[9]
                results.append(float(x))
        msg = str(sum(results)/len(results)) + \
            " was the average percent of correct answers"+"\n"
        return msg

    def give_summary_of_db(self):
        dat = self.data
        msg = "Currently database contains: " + "\n"

        # Sessions
        msg = msg + str(len(dat)) + " recorded sessions" + "\n" + \
            self.__describe_n_of_users(dat) + \
            self.__describe_n_of_input_files(dat) + \
            self.__describe_total_time(dat) + \
            self.__total_checked_questions(dat) + \
            self.__total_answered_questions(dat) + \
            self.__correctly_answered_questions(dat) + \
            self.__percentage_of_correct(dat)
        return msg
