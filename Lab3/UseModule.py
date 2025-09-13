# Test to see how the functions defined in HandyMath work.
# Name: Micah French
# Date: 09/12/2025


import HandyMath as HM


number1=float(input("Enter the first number: "))
number2=float(input("Enter the second number: "))


mid=HM.midpoint(number1, number2)
print("The midpoint between {number1} and {number2} is {mid}")


exp=HM.exponent(number1, number2)
print(f"{number1} raised to the {number2} power is {exp}")


max_number=HM.max(number1, number2)
print(f"The maximum of {number1} and {number2} is {max_number}")


min_number=HM.min(number1, number2)
print(f"The minimum of {number1} and {number2} is {min_number}")


sq_root = HM.square_root(number1)
print(f"The square root of {number1} is {sq_root}")