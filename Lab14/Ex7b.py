import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    base = os.path.dirname(__file__)
    csv_path = os.path.join(base, "taxi trips Fri 7_7_2017.csv")

    if not os.path.exists(csv_path):
        print(f"File not found: {csv_path}")
        return

    # read CSV (use chunksize if memory is a concern)
    df = pd.read_csv(csv_path, low_memory=False)

    # normalize column names and find target columns robustly
    cols = [c.lower().strip() for c in df.columns]
    col_map = dict(zip(cols, df.columns))  # map lowercase -> original
    pu_col = col_map.get("pickup_community_area") or col_map.get("pickup_community") or None
    do_col = col_map.get("dropoff_community_area") or col_map.get("dropoff_community") or None

    if not pu_col or not do_col:
        print("Could not find pickup_community_area / dropoff_community_area columns. Available:", df.columns.tolist())
        return

    # coerce to numeric (community areas are usually integers)
    df[pu_col] = pd.to_numeric(df[pu_col], errors="coerce")
    df[do_col] = pd.to_numeric(df[do_col], errors="coerce")

    # drop rows with missing community area
    df = df.dropna(subset=[pu_col, do_col]).astype({pu_col: int, do_col: int})

    # build contingency table (pickup x dropoff)
    ct = pd.crosstab(df[pu_col], df[do_col])

    # optional: sort index/columns numerically
    ct = ct.sort_index().reindex(sorted(ct.columns), axis=1)

    # plot heatmap
    plt.figure(figsize=(12, 10))
    sns.heatmap(ct, cmap="YlGnBu", norm=None)  # consider log scale or vmax for large ranges
    plt.title("Pickup vs Dropoff Community Area (counts)")
    plt.xlabel("Dropoff Community Area")
    plt.ylabel("Pickup Community Area")

    out_path = os.path.join(base, "pickup_dropoff_heatmap.png")
    plt.savefig(out_path, bbox_inches="tight", dpi=150)
    plt.close()
    print(f"Saved heatmap to {out_path}")

if __name__ == "__main__":
    main()