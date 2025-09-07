# Ask the user to enter a number between 1 and 100. Square the number
# and print the result to the console.
# Name: Micah French
# Date: 09/03/2025

value_entered = input("Please enter an integer between 1 and 100: ")
print("The user entered", value_entered)

# Convert the input string to a float for mathematical operations.
value_as_float = float(value_entered)

value_squared = value_as_float * value_as_float
print(f"The value squared is {value_squared}")