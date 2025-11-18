import os
import json
import pandas as pd
import matplotlib.pyplot as plt

def find_list_in_json(obj):
    if isinstance(obj, list):
        return obj
    if isinstance(obj, dict):
        for v in obj.values():
            if isinstance(v, list):
                return v
    return None

def find_column(df, keywords):
    cols = list(df.columns)
    for kw in keywords:
        for c in cols:
            if kw in c.lower():
                return c
    return None

def main():
    base = os.path.dirname(__file__)
    path = os.path.join(base, "Trips from area 8.json")
    if not os.path.exists(path):
        print(f"File not found: {path}")
        return

    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = find_list_in_json(data)
    if not records:
        print("No list of records found in JSON.")
        return

    df = pd.DataFrame(records)
    if df.empty:
        print("No records to process.")
        return

    # locate likely columns
    miles_col = find_column(df, ["mile", "distance"])
    fare_col = find_column(df, ["fare", "price", "total", "cost", "amount"])

    if not miles_col or not fare_col:
        print("Could not find miles or fare columns. Available columns:", df.columns.tolist())
        return

    # coerce to numeric and filter
    df[miles_col] = pd.to_numeric(df[miles_col], errors="coerce")
    df[fare_col] = pd.to_numeric(df[fare_col], errors="coerce")
    df = df.dropna(subset=[miles_col, fare_col])

    # Filter out 0 miles and < 2 miles (keep miles >= 2)
    df = df[df[miles_col] >= 2]

    if df.empty:
        print("No trips with miles >= 2 after filtering.")
        return

    # plot
    plt.figure(figsize=(8, 6))
    plt.scatter(df[miles_col], df[fare_col], alpha=0.6, edgecolors="none")
    plt.xlabel("Trip Miles")
    plt.ylabel("Fare ($)")
    plt.title("Fares vs Trip Miles (trips >= 2 miles)")
    plt.grid(True)
    out_path = os.path.join(base, "FaresXmiles.png")
    plt.savefig(out_path, bbox_inches="tight", dpi=150)
    plt.close()
    print(f"Saved scatter plot to {out_path}")

if __name__ == "__main__":
    main()