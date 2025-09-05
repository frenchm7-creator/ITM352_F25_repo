# Convert the user to enter a temperature in fahrenheit.
#Conver this to degrees Celcius and return the value to the user.
# Name: Micah French
# Date: 09/05/2025
degreesF = input("Enter temperature in degrees Fahrenheit: ")

degreesF_float = float(degreesF)
degreesC = (degreesF_float - 32) * 5.0/9.0
degreesC = round(degreesC)

print(f"{degreesF_float} degrees Fahrenheit is {degreesC} degrees Celsius.")