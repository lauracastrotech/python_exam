# This is a built in module for python
import unittest 

# This imports that functions that I want to test
from functions_ttt import *

# Create a test class that inherits from unittest.TestCase. Define methods within this # class to represent different test cases. Use # methods like assertEqual, assertTrue, 
# and assertFalse to check the results of your functions against expected values
class TestTicTacToe(unittest.TestCase):
    def test_display_board(self):
        # Write test cases for the check_game_state function

    def test_enter_move(self):
        # Write test cases for the make_move function

    def make_list_of_free_fields(self):
        # Write test cases for the check_for_win function

if __name__ == '__main__':
     unittest.main()