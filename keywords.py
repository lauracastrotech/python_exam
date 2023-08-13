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
            
a = A() # Assign an instance of the class to a variable
if print('hi') is None: #if this is True take this action
    a.f()
else:
    print('42')

a.f2 = lambda x: x+1 #assign lambda who value is x and expression is x+1
print(a.f2(41) in [1,2,42])