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
    def __init__(self, output_allowed=True):
        self.db_dir = os.path.join(os.getcwd(), "src", "data")
        self.output_allowed = output_allowed
        self.db_path = os.path.join(self.db_dir, "csv_database.csv")

        # SQL-database
        self.sql_db_path = os.path.join(self.db_dir, "database.db")

        self.database_interactions = DatabaseInteractions(
            self.sql_db_path, self.db_path)
        self.database_file_handling = DatabaseFileHandling(
            self.sql_db_path, self.db_dir, self.db_path, self.database_interactions)
        self.database_user_interactions = DatabaseUserInteractions(
            self.database_interactions)
        self.data = self.database_user_interactions.data[:]
