# This is a code sample from section 4.5.1.6 Creating functions: factorials
# Programmer: L Castro
# Date: 8/7/2023

def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    product = 1
    for number in range(2, n + 1):
        product *= number
    return product

#Test the factorial function
for n in range(1, 6):
    print(n, factorial_function(n))