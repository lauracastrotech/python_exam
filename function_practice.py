"""
Programmer: L Castro
Date: July 26, 2023
Purpose: The code below is Lab 4.3.1.6 to Lab 4.3.1.8 in module 4. This is practice
for writing functions.
"""
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False