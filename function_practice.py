"""
Programmer: L Castro
Date: July 26, 2023
Purpose: The code below is Lab 4.3.1.6 to Lab 4.3.1.8 in module 4. This is practice
for writing functions.
"""
def is_leap_year(year):
    # Function to determine a leap year
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
    
def get_days_in_month(year, month):
    # Function to get the number of days in a given month/year pair

    # List of days in each month (0 index represents January)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check if the month is valid (between 1 and 12)
    if month < 1 or month > 12:
        return None

    # Check if the year and month combination makes sense
    if month == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    else:
        return days_in_month[month - 1]
    
def day_of_year(year, month, day):
    # List of days in each month (0 index represents January)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Change day value from 28 to 29 in the days in month list when the year is a leap year
    if month == 2 and is_leap_year(year):
        days_in_month[1] = 29
        
    # Write conditional statement that ensures the month and day values are valid
    if (month < 1 or month > 12) or (day < 1 or day > 31):
        return None
    
    # Calculate the day of the year based on the year, month, and day
    day_of_year = sum(days_in_month[:month - 1]) + day
    
    return day_of_year

#Test Case 1
print(day_of_year(2000, 12, 31))
print(day_of_year(1989, 1, 12))