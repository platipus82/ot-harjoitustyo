import unittest
import os

class TestInputs(unittest.TestCase):
    def test_that_inputdir_exists(self):
        print(os.getcwd())
        pth = "D:\OT23\ot-harjoitustyo\src\inputs" 
        pthExists =  os.path.exists(pth) 
        self.assertEqual(True, pthExists)

    #def test_that_inputdir_is_not_empty(self):
        
    def test_that_inputfile_exists(self):
        pth = "D:\OT23\ot-harjoitustyo\src\inputs\Topic1.txt"
        pthExists =  os.path.isfile(pth) 
        self.assertEqual(True, pthExists)

    def test_that_inputfile_is_not_empty(self):
        fl = open("D:\OT23\ot-harjoitustyo\src\inputs\Topic1.txt")
        empty = True
        for r in fl:
            if r!="": empty = False
        self.assertEqual(False, empty)

    #def test_that_inputfile_rows_are_identical(self):
        




