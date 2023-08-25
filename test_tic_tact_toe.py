# This is a built in module for python
import unittest 

# This gives access to the random module that is used by the function that draws the computer's move
import random

# This imports that functions that I want to test
from tic_tact_toe import display_board, enter_move, make_list_of_free_fields, victory_for, draw_move

# Create a class that is a subclass to the test case class of the unit test module. Test methods are written in this class.
class TestTicTactToe(unittest.TestCase):
    
    # A test method must start with the word test. Write a test method for each function in the program
    def test_display_board(self):
        pass
  
    def test_enter_move(self):
        pass
    
    def test_make_list_of_free_fields(self):
        pass
    
    def test_victory_for(self):
        pass
    
    def test_draw_move(self):
        pass