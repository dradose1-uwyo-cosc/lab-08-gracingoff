# Gracin Goff
# UWYO COSC 1010
# 11/05/2024
# Lab 08
# Lab Section: 10
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 

def conversion(num):
    isneg = False
    if num[0] == "-":
        isneg = True
        num = num.replace("-","")
    if "." in num:
        num_dec = num.split(".")
        if len(num_dec) == 2 and num_dec[0].isdigit() and num_dec[1].isdigit():
            if isneg:
                return -1*float(num)
            else:
                return float(num)
    elif num.isdigit():
        if isneg :
            return -1*(num)
        else:
            return int(num)
    else:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list


def slope_intercept():
    while True:
        m = input("Give me a value for a slope")
        if m.upper() == "EXIT":
            break
        else:
            m = conversion(m)
        b = input("Give me a number for a y-intercept")
        if b.upper() == "EXIT":
            break
        else:
            b = conversion(b)
        lower = input("Give me a number for a lower bound")
        if lower.upper() == "EXIT":
            break
        else:
            lower = conversion(lower)
        upper = input("Give me a value for an upper bound")
        if upper.upper() == "EXIT":
            break
        else:
           upper = conversion(upper)
        if lower >= upper:
            print("Make sure lower bound is less than upperbound")
            lower = input("Give me a number for a lower bound")


slope_intercept()

point_slope = "y={m}x+{b}"
print(point_slope)

y_values = []

for i in range(lower_bound, upper_bound +1):

    y_values.append(m(i)+b)



print("*" * 75)


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
