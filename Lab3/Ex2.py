#Create a function called midpoint that takes two numbers as input 
# and return the value halfway between them.
# Name: Micah French
# Date: 09/10/2025

def midpoint(num1, num2):
    mid = (num1 + num2) / 2
    return mid
number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))
result = midpoint(number1, number2)
print(f"The midpoint between {number1} and {number2} is {result}")

