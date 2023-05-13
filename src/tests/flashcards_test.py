import unittest
import os
import sqlite3
#from src.flashcards import App
#from src.flashcards import Play
#from ui.ui import UI

#from flashcards import App
from processes.app import App
from processes.play import Play
from processes.database import Database

class TestApp(unittest.TestCase):
    def setUp(self):
        self.play=Play() 
        self.appi = self.play.game
        self.db = self.play.db
        #self.appi = App()

    def test_that_inputdir_exists_v2(self):
        print("Function test_that_inputdir_exists_v2()")
  
        pth=self.appi.input_dir
        #print(pth)
        pthExists =  os.path.exists(pth) 
        self.assertEqual(True, pthExists)

    def test_that_inputfilelist_not_empty(self):
        lst=self.appi.filelist
        self.assertEqual(False, len(lst)==0)
        
    def test_that_inputfile_exists(self):
        #pth = "D:\OT23\ot-harjoitustyo\src\inputs\Topic1.txt"
        pth = self.appi.input_path
        pthExists =  os.path.isfile(pth) 
        self.assertEqual(True, pthExists)

    def test_that_inputfile_is_not_empty(self):
        pth = self.appi.input_path
        fl = open(pth)
        empty = True
        for r in fl:
            if r!="": empty = False
        self.assertEqual(False, empty)


    def test_that_inputfile_is_formatted_correctly(self):
        pth = self.appi.input_path
        infile = open(pth)
        correct = True
        for line in infile:
            if line!="":
                if len(line.split(";"))!=2: correct = False
        self.assertEqual(True, correct)

    #def test_that_inputfile_rows_are_identical(self):
        
    #def test_that_give_summary_of_last_session(self): 

import unittest
from unittest.mock import mock_open, patch


class TestDatabase(unittest.TestCase):
  
    def setUp(self):
        #self.database = Database()
        self.db =Database()
        self.test_data = [['user1', 'deck1', '2023-05-12 12:00:00', '2023-05-12 12:10:00', '00:10:00', 10, 10, 10, 10, 100.0]]

    def test_get_db_data_success(self):
        test_data = ["1;John;Doe\n", "2;Jane;Smith\n", "3;Bob;Johnson\n"]
        expected_result = [["1", "John", "Doe\n"], ["2", "Jane", "Smith\n"], ["3", "Bob", "Johnson\n"]]
        with patch("builtins.open", mock_open(read_data="".join(test_data))):
            result = self.db.get_db_data()
        
        self.assertTrue(result)
        self.assertEqual(self.db.data, expected_result)
        
    def test_get_db_data_failure(self):
        with patch("builtins.open", side_effect=OSError):
            result = self.db.get_db_data()
        
        self.assertFalse(result)
        self.assertIsNone(self.db.data)

"""
    def tearDown(self):
        # Delete the test data from the database
        db = sqlite3.connect(self.db.sql_db_path)
        c = db.cursor()
        c.execute("DELETE FROM Records WHERE user='user1' AND deck='deck1'")
        db.commit()
        db.close()

    def test_write_to_sql_db(self):
        # Write the test data to the database
        self.db.write_to_sql_db(self.test_data)

        # Verify that the data was correctly inserted into the database
        db = sqlite3.connect(self.db.sql_db_path)
        c = db.cursor()
        c.execute("SELECT * FROM Records WHERE user='user1' AND deck='deck1'")
        rows = c.fetchall()
        self.assertEqual(len(rows), 1)        
        self.assertEqual(rows[0][1:], self.test_data[0])
        db.close()
"""

if __name__ == '__main__':
    unittest.main()

