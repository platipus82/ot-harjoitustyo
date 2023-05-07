#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 7 May 2023

@author: ok
'''

import os
import csv
from ui.ui import UI

class Database:
    def __init__(self, ui=UI(), output_allowed=True):
        self.__ui=ui
        self.db_dir = os.getcwd() + "\src\repositories\\"
        if not os.path.isfile(self.db_dir):
            self.db_dir = os.getcwd() + "/src/repositories/"        
        self.output_allowed = output_allowed
        self.db_path = self.db_dir + "csv_database.csv"
        self.data = []
        if not os.path.isfile(self.db_path):
            self.make_new_db_file()
        print(self.db_dir)
        print(self.db_path)

        
    def make_db_dir(self):
        #check if the input folder exists and has files
        if os.path.exists(self.db_dir) and os.path.isdir(self.db_dir): 
            pass
        else:
            os.mkdir(self.db_dir)

    def tell_db_colnames(self):
        cols = [["user", "deck", "start_time", "end_time", "elapsed_time", "questions_n_total", "questions_n_answered", "questions_n_correct", "questions_percent_correct"]]
        return cols
        
    def make_new_db_file(self):
        self.write_file(output_csv_file=self.db_path, rows_to_write=self.tell_db_colnames(), mode="w")
    
    def write_to_db(self, output_csv_file="", rows_to_write=[], mode="a"):
        self.write_file(output_csv_file=self.db_path, rows_to_write=rows_to_write, mode="a")
        
    def write_file(self, output_csv_file="", rows_to_write=[], mode="a"):
        try:
            with open(output_csv_file, mode, newline='') as myfile:
                filewriter = csv.writer(myfile, quoting=csv.QUOTE_NONE, delimiter=";")
                for r in rows_to_write:
                    filewriter.writerow(r)       
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
                        lines.append([items])
                        i += 1
                self.data = lines
                return True
        except OSError:
            return False
    
    def give_summary_data(self):
        self.get_db_data()
        all_results = self.data
        #print(all_results)
        return all_results
    
    def print_summary(self):
        results = self.give_summary_data()
        
        this = self.give_summary_of_last_session()
        all = self.give_summary_of_db()
        msg = this + all
        self.__ui.show_output(msg)
        #for x in results:
        #    print(x)
    
    def give_summary_of_last_session(self):
        msg = ""
        last = self.data[-1]
        last = last[0]
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
                user = entry[0][0]
                users.append(user)
        users = list(set(users))
        msg = msg + str(len(users)) + " different users" +"\n" 

        
        # n of input files
        infiles = []
        for i,entry in enumerate(dat):
            if i!=0:
                infile = entry[0][1]
                infiles.append(infile)
        infiles = list(set(infiles))
        msg = msg + str(len(infiles)) + " different decks (input files) have been used" +"\n" 
        
        # total time
        times = []
        for i,entry in enumerate(dat):
            if i!=0:
                used_time = entry[0][4]
                times.append(int(used_time))
        total_time = sum(times)
        msg = msg + str(total_time) + " seconds has been spent in total"+"\n" 
        
        # total answered questions
        questions = []
        for i,entry in enumerate(dat):
            if i!=0:
                nquest = entry[0][6]
                questions.append(int(nquest))
        msg = msg + str(sum(questions)) + " questions have been answered in total"+"\n" 
        
        # correctly answered questions
        questions = []
        for i,entry in enumerate(dat):
            if i!=0:
                nquest = entry[0][7]
                questions.append(int(nquest))
        msg = msg + str(sum(questions)) + " questions have been answered correctly"+"\n" 
        
        # percentage of correct 
        results = []
        for i,entry in enumerate(dat):
            if i!=0:
                x = entry[0][8]
                results.append(float(x))
        msg = msg + str(sum(results)/len(results)) + " was the average percent of correct answers"+"\n" 
        return msg
