from unittest.mock import mock_open, patch
import unittest
import os
import sqlite3
import tempfile

from processes.app import App
from processes.play import Play
from ui.user_interface import UserInterface
from repositories.database import Database, DatabaseFileHandling, DatabaseInteractions, DatabaseUserInteractions
from flashcards import main


class TestPlay(unittest.TestCase):
    def test_update_question_counters(self):
        """ Creating an instance of the class which contains the update_question_counters function"""
        obj = Play()

        # Set up the necessary preconditions
        obj.questions_n_correct = 0
        obj.questions_n_answered = 0
        obj._Play__ui.last_question_correct = True

        # Call the function to be tested
        obj.update_question_counters()

        # Assert the expected results
        self.assertEqual(obj.questions_n_correct, 1)
        self.assertEqual(obj.questions_n_answered, 1)

        # Test with another scenario
        obj._Play__ui.last_question_correct = False
        obj.update_question_counters()
        self.assertEqual(obj.questions_n_correct, 1)
        self.assertEqual(obj.questions_n_answered, 2)


class TestApp(unittest.TestCase):
    def setUp(self):
        self.play = Play()
        self.appi = self.play.game
        self.db = self.play.database

    def test_that_inputdir_exists_v2(self):
        pth = self.appi.input_dir
        pthExists = os.path.exists(pth)
        self.assertEqual(True, pthExists)

    def test_that_inputfilelist_not_empty(self):
        lst = self.appi.filelist
        self.assertEqual(False, len(lst) == 0)

    def test_that_inputfile_exists(self):
        pth = self.appi.input_path
        pthExists = os.path.isfile(pth)
        self.assertEqual(True, pthExists)

    def test_that_inputfile_is_not_empty(self):
        pth = self.appi.input_path
        fl = open(pth)
        empty = True
        for r in fl:
            if r != "":
                empty = False
        self.assertEqual(False, empty)

    def test_that_inputfile_is_formatted_correctly(self):
        pth = self.appi.input_path
        infile = open(pth)
        correct = True
        for line in infile:
            if line != "":
                if len(line.split(";")) != 2:
                    correct = False
        self.assertEqual(True, correct)

    # def test_that_inputfile_rows_are_identical(self):

    # def test_that_give_summary_of_last_session(self):


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.test_data = [['user1', 'deck1', '2023-05-12 12:00:00',
                           '2023-05-12 12:10:00', '00:10:00', 10, 10, 10, 10, 100.0]]

    def test_get_db_data_success(self):
        test_data = ["1;John;Doe\n", "2;Jane;Smith\n", "3;Bob;Johnson\n"]
        expected_result = [["1", "John", "Doe\n"], [
            "2", "Jane", "Smith\n"], ["3", "Bob", "Johnson\n"]]
        with patch("builtins.open", mock_open(read_data="".join(test_data))):
            result = self.db.database_interactions.get_db_data()

        self.assertTrue(result)
        self.assertEqual(self.db.database_interactions.data, expected_result)

    def test_get_db_data_failure(self):
        with patch("builtins.open", side_effect=OSError):
            result = self.db.database_interactions.get_db_data()

        self.assertFalse(result)
        self.assertEqual(self.db.data, [])


class TestDatabaseFileHandling(unittest.TestCase):
    def setUp(self):
        self.db_path = "test.db"
        self.db_file_handling = DatabaseFileHandling(sql_db_path=self.db_path, db_dir="", db_path="",
                                                     database_interactions=DatabaseInteractions(sql_db_path="", db_path=""))

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_make_new_sql_db_file(self):
        # Call the function to create the new SQL database file
        self.db_file_handling.make_new_sql_db_file()

        # Verify that the table is created in the database file
        db = sqlite3.connect(self.db_path)
        cursor = db.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name='Records';")
        result = cursor.fetchone()
        db.close()

        self.assertIsNotNone(result)
        self.assertEqual(result[0], "Records")


if __name__ == '__main__':
    unittest.main()
