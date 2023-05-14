#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Created on 30 Apr 2023

@author: ok
'''

import os
import random
from ui.gui import GUI
from ui.gui_input_file_selection import GUI_input_file_selection


class UI:
    """Class responsible for user interactions. If I/O is allowed, it will activate GUI-class responsible for GUI"""

    def __init__(self, use_default_input=True, output_allowed=False):
        """Class constructor.
        Arguments: 
            use_default_input: boolean parameter telling whether we want to proceed with default inputs for testing purposes, or not
            output_allowed:  boolean parameter telling whether (graphical) output is allowed or should be omitted
        """
        self.default_input = use_default_input
        self.output_allowed = output_allowed
        self.__gu = None
        self.mode = 0
        self.last_question_correct = False
        self.last_question_answered = False
        self.exit = False

    def show_output(self, output_text=""):
        """Function will ask GUI to show the output - if output is allowed. 
        Arguments:
            output_text: output text
        """
        if self.output_allowed:  # == True:
            self.__gu = GUI(use_default_input=False, output_allowed=True)
            self.__gu.show_output(output_text)

    def ask_for_input(self, output_text=""):
        """Function which will ask GUI to ask for user input. Function will receive user input from GUI and send it back for processing to the calling function.
        Arguments:
            output_text: text which will be showed to the user
        """
        resp = None
        if self.output_allowed:  # == True
            self.__gu = GUI(use_default_input=False, output_allowed=True)
            resp = self.__gu.ask_for_input(output_text)
        return resp

    def ask_for_input_file(self):
        """Function will GUI to ask user to choose the correct input file. Selected file will be sent back for processing to the calling function."""

        if self.output_allowed:  # == True:
            self.__gu = GUI_input_file_selection()
            resp = self.__gu.input_file_path
        return resp

    def ask_for_text(self, output_text=""):
        # print("UI.ask_for_input")

        resp = None
        if self.output_allowed == True:
            # resp = input(output_text)
            gu = GUI(use_default_input=False, output_allowed=True)
            resp = gu.ask_for_text(output_text)
        return resp

    def ask_for_text_timed(self, output_text="", timeout=0):
        resp = None
        if self.output_allowed == True:
            gu = GUI(use_default_input=False, output_allowed=True)
            resp = gu.ask_for_text_timed(output_text, timeout)
        return resp

    def set_mode(self):
        if not self.output_allowed:
            self.mode = 0
            return 0
        if self.output_allowed == True:
            # print("UI.set_mode()")

            msg0 = "Please, choose game mode: \n"
            msg1 = "  1. green: show question and answer simultaneously\n"
            msg2 = "  2. blue: show question first, then the correct answer\n"
            msg3 = "  3. red: show question first, than you can answer, then the program will evaluate your answer and show the correct answer\n"
            msg4 = "  4. black: same as red but with time-limit for each answer\n"
            msg5 = "  ....choose 1, 2, 3 or 4\n"

            msg = msg0+msg1+msg2+msg3+msg4+msg5
            resp = self.ask_for_text(output_text=msg)
            resp = str(resp).strip()

            if resp in ["1", "2", "3", "4"]:
                self.mode = int(resp)
                return self.mode
            elif resp == "x":
                msg = "You chose to exit the program. \nGAME OVER"
                self.show_output(output_text=msg)
                return "x"
            else:
                self.set_mode()

    def ask(self, question="", answer="", last_question=False):
        resp = None
        if self.mode == 0:
            resp = "x"
        elif self.mode == 1:
            resp = self.ask_mode1(
                question=question, answer=answer, last_question=last_question)
        elif self.mode == 2:
            resp = self.ask_mode2(
                question=question, answer=answer, last_question=last_question)
        elif self.mode == 3:
            resp = self.ask_mode3(
                question=question, answer=answer, last_question=last_question)
        elif self.mode == 4:
            resp = self.ask_mode4(
                question=question, answer=answer, last_question=last_question)
        return resp

    def ask_mode1(self, question="", answer="", last_question=False):
        # print("Function ask_mode1()")
        msg = "Question: " + question + "\n" + "Correct answer: " + answer + "\n"
        if last_question == False:
            msg = msg + "Proceed to the next question? "
            resp = self.ask_for_input(output_text=msg)
        else:
            msg = msg + "This was the last question! Well done!"
            self.show_output(output_text=msg)
            return "x"
        if resp == "x":
            msg = "GAME OVER"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

    def ask_mode2(self, question="", answer="", last_question=False):
        msg_pt1 = "Please, press proceed to see the correct answer" + "\n"
        msg_pt2 = "Press exit to exit the application" + "\n"
        msg = "Question: " + question + "\n" + msg_pt1 + msg_pt2
        resp = self.ask_for_input(output_text=msg)

        if resp == "x":
            msg = "GAME OVER"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

        msg = "Question: " + question + "\n" + "Answer: " + answer + "\n"

        if last_question == False:
            msg = msg + "Proceed to the next question? "
            resp = self.ask_for_input(output_text=msg)
            return
        else:
            msg = msg + "This was the last question! Well done!"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

        if resp == "x":
            msg = "GAME OVER"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

    def ask_mode3(self, question="", answer="", last_question=False):
        msg_pt1 = "Please, write your answer and press Submit" + "\n"
        msg_pt2 = "Press X to eXit the application" + "\n"
        msg = "Question: " + question + "\n" + msg_pt1 + msg_pt2
        resp = self.ask_for_text(output_text=msg)

        # removing trailing and leading empty spaces
        answer = str(answer).strip()
        resp = str(resp).strip()
        if resp == "x":
            msg = "GAME OVER"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

        msg_pt1 = "Question: " + question + "\n"
        msg_pt2 = "Your answer: " + resp + "\n"
        if str(resp) == str(answer):
            msg_pt3 = "Your answer is correct" + "\n"
            self.last_question_correct = True
        else:
            msg_pt3 = "Your answer is incorrect" + "\n"
            self.last_question_correct = False

        msg_pt4 = "Correct answer: " + answer + "\n"
        msg = msg_pt1 + msg_pt2 + msg_pt3 + msg_pt4

        if last_question == False:
            msg = msg + "Next question? "
            resp = self.ask_for_input(output_text=msg)
        else:
            msg = msg + "This was the last question! Well done!"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

        if resp == "x":
            msg = "GAME OVER"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

    def ask_mode4(self, question="", answer="", last_question=False):
        timeout = 10
        msg_pt1 = "Please, write your answer and press Proceed" + "\n"
        msg_pt2 = "Press X to eXit the application" + "\n"
        msg = "Question: " + question + "\n" + msg_pt1 + msg_pt2
        resp = self.ask_for_text_timed(output_text=msg, timeout=timeout)

        # removing trailing and leading empty spaces
        answer = str(answer).strip()
        resp = str(resp).strip()

        if resp == "x":
            msg = "GAME OVER"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"
        elif resp == "timeout":
            msg = "You ran out of time. GAME OVER."
            self.show_output(output_text=msg)
            self.exit = True
            return "x"
        else:
            self.last_question_answered = True

        msg_pt1 = "Question: " + question + "\n"
        msg_pt2 = "Your answer: " + resp + "\n"
        if str(resp) == str(answer):
            msg_pt3 = "Your answer is correct" + "\n"
            self.last_question_correct = True
        else:
            msg_pt3 = "Your answer is incorrect" + "\n"
        msg_pt4 = "Correct answer: " + answer + "\n"
        msg = msg_pt1 + msg_pt2 + msg_pt3 + msg_pt4

        if last_question != True:
            msg = msg + "Next question? "
            resp = self.ask_for_input(output_text=msg)
        else:
            msg = msg + "This was the last question! Well done!"
            self.show_output(output_text=msg)
            self.exit = True
            return

        if resp == "x":
            msg = "GAME OVER"
            self.show_output(output_text=msg)
            self.exit = True
            return "x"

        elif resp == "timeout":
            msg = "You ran out of time. GAME OVER."
            self.show_output(output_text=msg)
            self.exit = True
            return
        else:
            return


if __name__ == "__main__":
    import os
    from ui.ui import GUI
    from ui.ui import GUI_input_file_selection

    main()
