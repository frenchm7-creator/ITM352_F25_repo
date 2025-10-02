def determine_progress1(year):
    messages = ["Not a leap year", "Leap year"]
    index = int((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))
    return messages[index]

year = int(input("Enter a year: "))
print(determine_progress1(year))