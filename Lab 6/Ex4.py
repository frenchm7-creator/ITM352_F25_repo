my_birth_year = 2005
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# Test with your birth year
if (my_birth_year % 4 == 0 and my_birth_year % 100 != 0) or (my_birth_year % 400 == 0):
    print(f"{my_birth_year} is a Leap year")
else:
    print(f"{my_birth_year} is Not a leap year")