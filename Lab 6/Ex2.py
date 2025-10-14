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

# Test cases for each possible condition
# Each sublist contains the input and the expected output description

test_cases = [
    [0, "Short list"],      # listOfLists[0] is []
    [1, "Short list"],      # listOfLists[1] has 3 elements
    [2, "Medium list"],     # listOfLists[2] has 7 elements
    [3, "Long list"],       # listOfLists[3] has 12 elements
    [4, "Invalid"],         # Out of range
    [-1, "Invalid"],        # Negative index
    ["a", "Invalid"]        # Non-integer input
]