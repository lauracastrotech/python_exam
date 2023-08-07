# This is a code sample from section 4.5.1.6 Creating functions: Fibonacci numbers
# Programmer: L Castro
# Date: 8/7/2023

# Write a function that takes an integer as an argument
def fib(n):
    # if the integer is less than 1, than it is invalid
    if n < 1:
        return None
    # if the integer is the number 1 or 2, the fibonacci number is 1
    if n < 3:
        return 1
    
    # initialize the first two elements, which will be 1
    element_1 = element_2 = 1
    
    # initialize a variable to store the sum of elements 
    the_sum = 0
    
    # starting with the number 3, check every number up to the number + 1

