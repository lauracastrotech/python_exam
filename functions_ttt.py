#This file stores all of the functions for the tic tac toe program

# This function accepts one parameter containing the board's current status and prints it out to the console.
def display_board(board):
    for row in range(0,3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(" ")
        for column in range(0,3): #This loop prints the value of each square on the board
            print("|  ", board[row][column], " ", end=" ")
        print("|")
        print(" ")
        print("|       |       |       |")
    print("+-------+-------+-------+")

# The function accepts the board's current status, asks the user about their move, checks the input, and updates the board according to the user's decision.
def enter_move(board, free_list):
    # Get the user's input and validate that it is an integer between 0 and 10 and it cannot point to a field in the free squares list
    user_move = int(input("Enter your move: "))
    if user_move > 0 and user_move < 10 and user_move in free_list:
        # Write a loop that will match the input with the square and update the element using the # index of the number
        for square in range(0,3):
            for number in range(0,3):
                if user_move == board[square][number]:
                    board[square][number] = 'O'
 


# This function browses the board and builds a list of all the free squares; the list consists of tuples, while each tuple is a pair of row and column numbers.
def make_list_of_free_fields(board, free_list):
    for index, column in enumerate(board): # iterate through the board and add the corresponding element from index to free squares list
        free_list.append(tuple(column)) # convert the column list to a tuple and add it to the free squares list, the this list will store integers and strings and the user can only select from the integer elements that represent a free space

# This function returns the value of the sign that is be checked for victory
def check_sign(letter):
    if letter == 'X':
        return 'You lose!'
    else:
        return 'You win!'
# This function analyzes the board's status in order to check if the player using 'O's or 'X's has won the game
def victory_for(board, sign):
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or \
       (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or \
       (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or \
       (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or \
       (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or \
       (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or \
       (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[1][2] == sign and board[1][1] == sign and board[2][0] == sign):
           print(check_sign(sign))