#Create a list of dictionaries where each dictionary represents
# a taxi trip with keys.
# Name: Micah French
# Date: 09/19/2025
taxiTrips = [
    {'duration': 1.1, 'fare': 6.25},
    {'duration': 2.3, 'fare': 12.50},
    {'duration': 0.5, 'fare': 3.75},
    {'duration': 4.0, 'fare': 20.00}
]
print(taxiTrips)
print(f"The third trip was {taxiTrips[2]['duration']} miles and cost ${taxiTrips[2]['fare'] * 0.8}.")
