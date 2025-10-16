listOfLists = [[], [1]*3, [2]*7, [3]*12]
print(listOfLists)

listNumber = int(input("Enter a list number (0-3): "))

if 0 <= listNumber < len(listOfLists):
    listLength = len(listOfLists[listNumber])
    if listLength < 5:
        print(f"User entered {listNumber}: Short list")
    elif 5 <= listLength <= 10:
        print(f"User entered {listNumber}: Medium list")
    else:
        print(f"User entered {listNumber}: Long list")
else:
    print("Invalid list number. Please enter a number between 0 and 3.")