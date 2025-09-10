# Create a module with handy math functions
# Name: Micah French
# Date: 09/10/2025

# Function to return the midpoint between two numbers
def midpoint(num1, num2):
    mid = (num1 + num2) / 2
    return mid

# Function to return the square root of a number
def square_root(x):
    if x < 0:
        raise ValueError("Error: Cannot compute square root of a negative number.")
    return x ** 0.5

# Function to return the result of raising base to the exponent exp
def exponent(base, exp):
    return base ** exp

# Function to return the maximum of two numbers
def max (a,b):
    return a if a > b else b

# Function to return the minimum of two numbers
def min (a,b):
    return a if a < b else b



