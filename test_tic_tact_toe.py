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
        # This is a visual function, so you might consider using other techniques like capturing stdout for more advanced testing
        # However, you can manually test if the function doesn't throw any errors
        board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]] # Initialized to a sample game state
        self.assertIsNone(display_board(board))  # Check if display_board doesn't raise an error
  
    def test_enter_move(self):
        board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
        with unittest.mock.patch('builtins.input', side_effect=['5', '7']):
            enter_move(board)
            self.assertEqual(board[2][0], 'O')  # Check if 'O' is placed in the correct position
    
    def test_make_list_of_free_fields(self):
        board = [[1, 'X', 3], [4, 'X', 6], [7, 8, 9]]
        free_squares = make_list_of_free_fields(board)
        self.assertCountEqual(free_squares, [1, 3, 4, 6, 7, 8, 9])  # Check if the list of free squares matches the expected values
    
    def test_victory_for(self):
        board = [[1, 2, 'O'], ['X', 'O', 'X'], ['O', 8, 9]]
        self.assertTrue(victory_for(board, 'O'))

        board = [[1, 2, 'O'], ['X', 'X', 'X'], ['O', 8, 9]]
        self.assertTrue(victory_for(board, 'X'))

    
    def test_draw_move(self):
        board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
        random.seed(42)  # Set a seed for reproducible randomness
        draw_move(board)
        self.assertEqual(board[0][0], 'X')  # Check if 'X' is placed in the correct position

if __name__ == '__main__':
    unittest.main()
    
   
