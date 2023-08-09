# Programmer: Laura Castro
# Date: August 9, 2023
# Purpose: This program solves a puzzle from an article about python keywords
# and will go through each keyword with examples

# This is the puzzle, guess the output
class A:
    def f(self):
        if False and True: #if False then take this action
            print('NO')
        elif not False or False: #if True or False take this action
            print('YES')
        else: #if anything else take this action
            print('MAYBE')
