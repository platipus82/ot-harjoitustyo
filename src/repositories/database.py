#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 May 2023

@author: ok
'''

import os

from ui.database_user_interactions import DatabaseUserInteractions
from repositories.database_file_handling import DatabaseFileHandling
from repositories.database_interactions import DatabaseInteractions


class Database:
    """
    Class representing a database and its interactions.

    Attributes:
        db_dir (str): The directory where the database files are stored.
        output_allowed (bool): Flag indicating if (graphical) output is allowed or not.
        db_path (str): The path to the CSV database file.
        sql_db_path (str): The path to the SQL database file.
        database_interactions (DatabaseInteractions): An instance of DatabaseInteractions for handling SQL database interactions.
        database_file_handling (DatabaseFileHandling): An instance of DatabaseFileHandling for handling CSV database interactions.
        database_user_interactions (DatabaseUserInteractions): An instance of DatabaseUserInteractions for describing data for the user.
        data (list): A list to store the data from the user interactions.
    """

    def __init__(self, output_allowed=True):
        """
        Class constructor.

        Args:
            output_allowed (bool): Flag indicating if (graphical) output is allowed or not.
        """

        self.db_dir = os.path.join(os.getcwd(), "src", "data")
        self.output_allowed = output_allowed
        self.db_path = os.path.join(self.db_dir, "csv_database.csv")
        self.sql_db_path = os.path.join(self.db_dir, "database.db")
        self.database_interactions = DatabaseInteractions(
            self.sql_db_path, self.db_path)
        self.database_file_handling = DatabaseFileHandling(
            self.sql_db_path, self.db_dir, self.db_path, self.database_interactions)
        self.database_user_interactions = DatabaseUserInteractions(
            self.database_interactions)
        self.data = self.database_user_interactions.data[:]
