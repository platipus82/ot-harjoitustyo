#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 May 2023

@author: ok
'''

import sqlite3


class DatabaseInteractions:
    """Class responsible for handling the storage information. 
    Handling involves reading, writing and describing the data. """

    def __init__(self, sql_db_path, db_path):
        """
        Class constructor. The constructor takes two input arguments/parameters:
                sql_db_path: The path to the SQL database file.
                db_path: The path to the CSV database file.
                These values are assigned to the corresponding instance variables 
                    - self.sql_db_path 
                    - self.db_path. 
                The self.data attribute is initialized as an empty list. 
        """
        self.sql_db_path = sql_db_path
        self.db_path = db_path
        self.data = []

    def tell_db_colnames(self):
        """Function will return the column names for the database"""
        cols = [["user", "deck", "start_time", "end_time",
                "elapsed_time", "questions_n_total",
                 "questions_n_checked", "questions_n_answered",
                 "questions_n_correct", "questions_percent_correct"]]
        return cols

    def get_db_data(self):
        """Function will extract and save the data from the csv-database"""

        try:
            with open(self.db_path, "r", encoding="utf-8") as infile:
                lines = []
                for line in infile:
                    if line != "":
                        items = line.split(";")
                        lines.append(items)
                self.data = lines
                return True
        except OSError:
            self.data = []  # None
            return False

    def get_sql_db_data(self):
        """Function will extract and save the data from the SQL-database"""
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
                if isinstance(x, float):
                    lista.append(str(round(y, 2)))
                else:
                    lista.append(str(y))
            lista.pop(0)
            listat.append(lista)
        self.data = listat
        return self.data
