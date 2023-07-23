#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 20 July 2023

@author: ok
'''

import os
import csv
import sqlite3
import time


class DatabaseFileHandling:
    """Class responsible for handling the database files.

    Attributes:
        sql_db_path (str): The path to the SQL database file.
        db_dir (str): The directory where the database files are stored.
        db_path (str): The path to the CSV database file.
        data (list): A list to store data from the database interactions.
        database_interactions (DatabaseInteractions): An instance of DatabaseInteractions class.

    Methods:
        __init__():
            Class constructor that initializes the attributes.
            Args:             
                sql_db_path: str, 
                db_dir: str, 
                db_path: str, 
                database_interactions: DatabaseInteractions
        make_new_sql_db_file():
            Creates a new SQL database file.
            Args: 
                alternative_pth: str=None
        make_db_dir():
            Checks if the input folder exists and has files. Creates it if needed.
        make_new_db_file():
            Creates a new .csv database file with column names.
        write_to_db():
            Writes data to an existing .csv database file.
            Args: 
                output_csv_file: str="",
                rows_to_write: list=None, 
                mode: str="a"
        write_to_sql_db():
            Writes data to the SQL database file.
            Args: 
                rows_to_write: list=None, 
                alternative_pth: str=None
        write_file():
            Writes data to a separate .csv file.
            Args: 
                output_csv_file: str="", 
                rows_to_write: list=None, 
                mode: str="a"

    """

    def __init__(self, sql_db_path, db_dir, db_path, database_interactions):
        """The constructor takes four parameters:
            - sql_db_path: The path to the SQL database file.
            - db_dir: The directory where the database files are stored.
            - db_path: The path to the CSV database file.
            - database_interactions: instance of DatabaseInteractions class

            These attributes are then assigned to the corresponding instance variables:  
                - self.sql_db_path, 
                - self.db_dir
                - self.db_path
                - self.database_interactions. 
            The self.data attribute is initialized as an empty list.
            Constructor will create new database files if they do not exist already.
        """

        self.sql_db_path = sql_db_path
        self.db_dir = db_dir
        self.db_path = db_path
        self.data = []
        self.database_interactions = database_interactions
        if not os.path.isfile(self.db_path):
            self.make_new_db_file()

        if not os.path.isfile(self.sql_db_path):
            self.make_new_sql_db_file()

    def make_new_sql_db_file(self, alternative_pth=None):
        """Function creating the new SQL database file."""
        if alternative_pth is None:
            pth = self.sql_db_path
        else:
            pth = alternative_pth
        database = sqlite3.connect(pth)
        database.isolation_level = None
        cursor = database.cursor()
        part1 = "CREATE TABLE IF NOT EXISTS Records "
        part2 = "(id TEXT NOT NULL, user TEXT NOT NULL, deck TEXT NOT NULL, "
        part3 = "start_time TEXT NOT NULL, end_time TEXT NOT NULL, "
        part4 = "elapsed_time TEXT NOT NULL, questions_n_total INTEGER, "
        part5 = "questions_n_checked INTEGER, questions_n_answered INTEGER, "
        part6 = "questions_n_correct INTEGER, questions_percent_correct REAL);"
        whole_command = part1+part2+part3+part4+part5+part6
        cursor.execute(whole_command)

    def make_db_dir(self):
        """ Function will check if the input folder exists and has files. 
            If new folder is needed, function will create it. """
        if os.path.exists(self.db_dir) and os.path.isdir(self.db_dir):
            pass
        else:
            os.mkdir(self.db_dir)

    def make_new_db_file(self):
        """Function will make a new .csv database file with column names"""
        self.write_file(output_csv_file=self.db_path,
                        rows_to_write=self.database_interactions.tell_db_colnames(), mode="w")

    def write_to_db(self, output_csv_file="", rows_to_write=None, mode="a"):
        """ Function will write to a existing .csv database file
            Args:
                output_csv_file (str, optional):
                    The path to the existing .csv database file. 
                    Default is an empty string.
                rows_to_write (list, optional): 
                    The list of rows to be written to the database. 
                    Default is None.
                mode (str, optional): 
                    The writing mode for the file 
                    Modes: "a" for append, "w" for write
                    Default is "a".
        """

        self.write_file(output_csv_file=output_csv_file,
                        rows_to_write=rows_to_write, mode=mode)  # mode="a"

    def write_to_sql_db(self, rows_to_write=None,  alternative_pth=None):
        """ Function will write to SQL-database file. 
            Args:
                rows_to_write (list, optional): 
                    The list of rows to be written to the SQL database. 
                    Default is None.
                alternative_pth (str, optional): 
                    An alternative path to the SQL database file. 
                    Default is None.
        """
        if alternative_pth is None:
            pth = self.sql_db_path
        else:
            pth = alternative_pth

        data = []
        for x in rows_to_write:
            # primary_key = x[2]
            # Append a timestamp to ensure uniqueness
            primary_key = f"{x[2]}_{int(time.time())}"
            x = [primary_key] + x
            data.append(x)
        database = sqlite3.connect(pth)  # self.sql_db_path
        database.isolation_level = None
        cursor = database.cursor()
        cursor.execute("BEGIN")
        whole_command = "CREATE TABLE IF NOT EXISTS Records (id STRING PRIMARY KEY, " + \
            "start_time TEXT NOT NULL, end_time TEXT NOT NULL, elapsed_time TEXT NOT NULL, " + \
            "questions_n_total INTEGER, questions_n_checked INTEGER, " + \
            "questions_n_answered INTEGER, " + \
            "questions_n_correct INTEGER, " + \
            "questions_percent_correct REAL);"
        cursor.execute(whole_command)
        whole_command = "INSERT INTO Records (" + \
            "id, user, deck, start_time, end_time, elapsed_time, questions_n_total," + \
            "questions_n_checked, questions_n_answered, questions_n_correct, " + \
            "questions_percent_correct )" + \
            "VALUES (?,?,?,?,?,?,?,?,?,?,?);"
        cursor.executemany(whole_command, data)
        cursor.execute("COMMIT")

    def write_file(self, output_csv_file="", rows_to_write=None, mode="a"):
        """Function will write text to .csv file. 
            Function expects text to write and file name. 
            If these are provided as an argument function:
                will write text to separate .csv file
                return True
            If no text is provided or it is in wrong format: 
                will return False.
        """
        try:
            with open(output_csv_file, mode, newline='', encoding="utf-8") as myfile:
                filewriter = csv.writer(
                    myfile, quoting=csv.QUOTE_NONE, delimiter=";")
                for row in rows_to_write:
                    filewriter.writerow(row)
            return True
        except OSError:
            return False
