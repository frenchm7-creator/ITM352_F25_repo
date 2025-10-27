# Read a file of questions from a JSON file and save them in a dictionary.
# Print the dictionary to the console.
import json

#Specify the JSON file name
JSON_file = "quiz.json"

#Open the file in read mode and load the JSON data into a dictionary
with open(JSON_file, "r") as json_file:
    data = json.load(json_file)

#Print the dictionary to the console
print(data)