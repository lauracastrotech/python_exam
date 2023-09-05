"""
Programmer: L Castro
Date: July 26, 2023
Purpose: The code below is Lab 4.3.1.6 to Lab 4.3.1.8 in module 4. This is practice
for writing functions.
"""
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

#Test Case 2
print(day_of_year(1989, 1, 12))

# Excercise from section summary
def is_int(data):
    if type(data) == int:
        return True
    elif type(data) == float:
        return False

print(is_int(5))
print(is_int(5.0))
print(type("5"))
    """

"""
#This is an example of using the global keyword
def a_function():
    global var
    var = 2
    return print("Is this a var", var)

var = 1
a_function()
print(var)

#Here is a simple function evaluating the BMI
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
       weight < 20 or weight > 200:
        return None
    #Return this if the value is valid
    return weight / height ** 2

#A function to convert pounds to kilograms
def lb_to_kg(lb):
    return lb * 0.45359237

#A function to convert feet and inches to meters, uses a default value for inches
def feet_and_inches_to_m(ft, inch = 0.0):
    return ft * 0.3048 + inch * 0.0254

print(feet_and_inches_to_m(6))
print(lb_to_kg(1))
print(bmi(63.3, 5))
print(bmi(weight = lb_to_kg(176), height=feet_and_inches_to_m(5, 7)))

#This is a function that builds a triangle
def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

#This function uses the heron formula to calculate the area of a triangle
def heron(a,b,c):
    p = (a+b+c)/2
    return (p * (p -a ) * (p-b) * (p-c))**0.5

#This function returns the area of a triangle and checks to see that it is a triangle
def area_of_triangle(a,b,c):
    if not is_a_triangle:
        return None
    return heron(a,b,c)

#This function checks if the triangle is a right triangle
def is_a_right_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    
#Get the size of the side as input
a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

#Get the area of a triangle using input values
print(area_of_triangle(a,b,c))

#Check if it is a triangle
if is_a_triangle(a,b,c):
    print("Yes, it can be a triangle.")
else:
    print("No, it can\'t be a triangle.")

print(is_a_triangle(5,3,4))
print(is_a_right_triangle(5, 3, 4))

print(is_a_triangle(1, 3, 4))
print(is_a_right_triangle(1,3,4))


iterate_this_list = [1, 2, 3, 4 ,5]
for number in iter(iterate_this_list):
    print(number)
    
lst1 = [2,3,5,6]
lst = [[x for x in range(3)] for y in range(3)]
print(lst)

print("a","b","c",sep="sep")
"""
foo = (1,2,3)
foo.index(0)