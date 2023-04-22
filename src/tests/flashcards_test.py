import unittest
import os
from src.flashcards import App
from src.flashcards import Play
from src.ui.ui import UI

#from flashcards import App
#from flashcards import Play
#from src.ui import ui

class TestApp(unittest.TestCase):
    def setUp(self):
        self.appi = App()

    def test_that_inputdir_exists_v2(self):
        pth=self.appi.input_dir
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

    #def test_that_inputfile_rows_are_identical(self):
        


if __name__ == '__main__':
    unittest.main()

