# Read a JSON file of a taxi trip daya and create a dataframe.
# Calculate the median fare.
import pandas as pd

taxi_df=pd.read_json("Taxi_Trips.json")

# print a summary of the database.
print(taxi_df.describe())
print(taxi_df.head())

# Print the median fare
print("Median fare: ", taxi_df["fare"].median())
