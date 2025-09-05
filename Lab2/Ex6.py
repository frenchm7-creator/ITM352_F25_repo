# Ask the user to enter their weight in pounds. Convert this weight to
# kilograms and return the value to the user.
# Name: Micah French
# Date: 09/05/2025


weight_in_pounds = input("Enter your weight in pounds: ")
weight_in_kilos = float(weight_in_pounds) * 0.45359237
weight_in_kilos_rounded = round(weight_in_kilos,)
print(f"You weigh {weight_in_kilos_rounded} in kilograms.")