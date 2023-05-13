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
        #print("Class Database")
        self.db_dir = os.getcwd() + "\src\repositories\\"
        if not os.path.isfile(self.db_dir):
            self.db_dir = os.getcwd() + "/src/repositories/"        
        self.output_allowed = output_allowed
        
        # .csv database
        self.db_path = self.db_dir + "csv_database.csv"
        self.data = []
        if not os.path.isfile(self.db_path):
            self.make_new_db_file()
        #print(self.db_dir)
        #print(self.db_path)
        
        # SQL-database
        self.sql_db_path = self.db_dir + "database.db"
        if not os.path.isfile(self.sql_db_path):
            self.make_new_sql_db_file()

        # Summary
        self.summary = ""
        self.make_summary()

    def make_summary(self):
        results = self.give_summary_data()
        this = self.give_summary_of_last_session()
        all = self.give_summary_of_db()
        msg = this + all

        self.summary=msg

    def make_new_sql_db_file(self):
        db = sqlite3.connect(self.sql_db_path)
        db.isolation_level = None
        c = db.cursor()
        
        # Step 1: creating an empty table
        #print("...1: Creating an empty table if one does not exist yet.")
        c.execute("CREATE TABLE IF NOT EXISTS Records (id TEXT NOT NULL, user TEXT NOT NULL, deck TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL, elapsed_time TEXT NOT NULL, questions_n_total INTEGER, questions_n_checked INTEGER, questions_n_answered INTEGER, questions_n_correct INTEGER, questions_percent_correct REAL);")
  
    def make_db_dir(self):
        #check if the input folder exists and has files
        if os.path.exists(self.db_dir) and os.path.isdir(self.db_dir): 
            pass
        else:
            os.mkdir(self.db_dir)

    def tell_db_colnames(self):
        cols = [["user", "deck", "start_time", "end_time", "elapsed_time", "questions_n_total", "questions_n_checked", "questions_n_answered", "questions_n_correct", "questions_percent_correct"]]
        return cols
        
    def make_new_db_file(self):
        self.write_file(output_csv_file=self.db_path, rows_to_write=self.tell_db_colnames(), mode="w")
    
    def write_to_db(self, output_csv_file="", rows_to_write=[], mode="a"):
        self.write_file(output_csv_file=self.db_path, rows_to_write=rows_to_write, mode="a")
    
    def write_to_sql_db(self, rows_to_write=[]):
        headers = self.tell_db_colnames()[0]
        data = []
        for x in rows_to_write:
            id = x[2]
            x = [id] + x
            data.append(x)
            
        #for x in data:
        #    print(x)
        db = sqlite3.connect(self.sql_db_path)
        db.isolation_level = None
        c = db.cursor()
        c.execute("BEGIN")
        
        # id, user, deck, start_time, end_time, elapsed_time, questions_n_total, 
        # questions_n_answered, questions_n_correct, questions_percent_correct 
        c.execute("CREATE TABLE IF NOT EXISTS Records (id STRING PRIMARY KEY, user TEXT NOT NULL, deck TEXT NOT NULL, start_time TEXT NOT NULL, end_time TEXT NOT NULL, elapsed_time TEXT NOT NULL, questions_n_total INTEGER, questions_n_checked INTEGER, questions_n_answered INTEGER, questions_n_correct INTEGER, questions_percent_correct REAL);")
        c.executemany("INSERT INTO Records (id, user, deck, start_time, end_time, elapsed_time, questions_n_total, questions_n_checked, questions_n_answered, questions_n_correct, questions_percent_correct ) VALUES (?,?,?,?,?,?,?,?,?,?,?);", data) 
        c.execute("COMMIT")
        
        
    def write_file(self, output_csv_file="", rows_to_write=[], mode="a"):
        try:
            with open(output_csv_file, mode, newline='') as myfile:
                filewriter = csv.writer(myfile, quoting=csv.QUOTE_NONE, delimiter=";")
                for r in rows_to_write:
                    filewriter.writerow(r)       
            return True
        except (OSError):
            return False       

    
    def get_db_data(self):
        try:
            with open(self.db_path, "r", encoding="utf-8") as infile:
                lines = []
                i=0
                for line in infile:
                    if line != "" :
                        items = line.split(";")
                        lines.append(items)
                        i += 1
                self.data = lines
                return True
        except OSError:
            self.data = None
            return False
        
    def get_sql_db_data(self):
        db = sqlite3.connect(self.sql_db_path)
        db.isolation_level = None
        c = db.cursor()
        c.execute("BEGIN")
        data = c.execute("SELECT * FROM Records;").fetchall()
        db.close()
        listat =[]
        for d in data:
            lista = []
            for x in d:
                lista.append(str(x))
            lista.pop(0)
            listat.append(lista)
        self.data = listat 

        
    def give_summary_data(self):      
        self.get_sql_db_data()
        db_db = self.data
        all_results = self.data
        return all_results
    
    def give_summary(self):
        return self.summary


    
    def give_summary_of_last_session(self):
        msg = ""
        #print(self.data)
        last = self.data[-1]
        last = last
        msg = msg + "Summary of this session:" +"\n"        
        cols = self.tell_db_colnames()[0]
        for i,entry in enumerate(last):
            #print(cols[i] + ": " + entry)
            msg = msg + cols[i] + ": " + entry +"\n" 
        return msg
    
    def give_summary_of_db(self):
        dat = self.data
        msg = ""
        msg = msg + "Currently database contains: " +"\n" 

        # Sessions
        msg = msg + str(len(dat)) + " recorded sessions" +"\n" 
        
        # n of users
        users = []
        for i,entry in enumerate(dat):
            if i!=0:
                user = entry[0]
                users.append(user)
        users = list(set(users))
        msg = msg + str(len(users)) + " different users" +"\n" 

        
        # n of input files
        infiles = []
        for i,entry in enumerate(dat):
            if i!=0:
                infile = entry[1]
                infiles.append(infile)
        infiles = list(set(infiles))
        msg = msg + str(len(infiles)) + " different decks (input files) have been used" +"\n" 
        
        # total time
        times = []
        for i,entry in enumerate(dat):
            if i!=0:
                used_time = entry[4]
                times.append(int(used_time))
        total_time = sum(times)
        msg = msg + str(total_time) + " seconds has been spent in total"+"\n" 
        cols = [["user", "deck", "start_time", 
                 "end_time", "elapsed_time", "questions_n_total", 
                 "questions_n_checked", "questions_n_answered", "questions_n_correct", 
                 "questions_percent_correct"]]


        # total checked questions
        questions = []
        for i,entry in enumerate(dat):
            if i!=0:
                nquest = entry[6]
                questions.append(int(nquest))
        msg = msg + str(sum(questions)) + " questions have been viewed in total"+"\n" 
                
        # total answered questions
        questions = []
        for i,entry in enumerate(dat):
            if i!=0:
                nquest = entry[7]
                questions.append(int(nquest))
        msg = msg + str(sum(questions)) + " questions have been answered in total"+"\n" 
        
        # correctly answered questions
        questions = []
        for i,entry in enumerate(dat):
            if i!=0:
                nquest = entry[8]
                questions.append(int(nquest))
        msg = msg + str(sum(questions)) + " questions have been answered correctly"+"\n" 
        
        # percentage of correct 
        results = []
        for i,entry in enumerate(dat):
            if i!=0:
                x = entry[9]
                results.append(float(x))
        msg = msg + str(sum(results)/len(results)) + " was the average percent of correct answers"+"\n" 
        return msg