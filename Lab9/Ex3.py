# Read the 1,000 lines of taxi data from the taxi_1000.csv file
#calculate the total of all fares, and the maximum trip distance
import csv

with open("taxi_1000.csv", "r", newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    total_fare = 0.0               # total of fares > $10
    max_distance = 0.0             # max distance among fares > $10
    qual_count = 0                 # count of qualifying records

    for row_index, row in enumerate(csv_reader):
        if row_index == 0:
            continue  # skip header row
        try:
            tripfare = float(row[10])
            distance = float(row[5])
        except (IndexError, ValueError):
            # skip malformed rows
            continue

        if tripfare > 10.0:
            total_fare += tripfare
            qual_count += 1
            if distance > max_distance:
                max_distance = distance

    if qual_count > 0:
        average_fare = round(total_fare / qual_count, 2)
        print(f"Records with fare > $10: {qual_count}")
        print(f"Total of fares > $10: ${total_fare:.2f}")
        print(f"Average fare (for fares > $10): ${average_fare:.2f}")
        print(f"Maximum trip distance (for fares > $10): {max_distance}")
    else:
        print("No records with fare > $10 found.")
