# Define a list of taxi trip durations in miles (with values 1.1, 0.8, 2.5, 2.6)
# Define a tuple of fares for the same trips (with values 6.25, 5.25, 10.50, 8.05)
# Store the tuple and list as values in a dictionary with keys
# "miles" and "fares"
# Name: Micah French
# Date: 09/19/2025
trip_durations = [1.1, 0.8, 2.5, 2.6]
trip_fares = (6.25, 5.25, 10.50, 8.05)

trips= {
    "miles": trip_durations,
    "fares": trip_fares
}
print(trips)
print(f"The duration of the third trip is {trips['miles'][2]} miles")
print(f"The cost of the third trip is ${trips['fares'][2]:.2f}")

trips["miles"].append(2.2)
trips["fares"] += (4.0,)
print(trips)

trip_num = int(input("What trip do you want?:"))
print(f"Duration: {trips['miles'][trip_num-1]} miles")

