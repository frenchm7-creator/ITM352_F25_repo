# Read in a CSV file and create a dataframe.  Print some info.
# Pivot the dataframe to show total and average sales by state and sale type.
import pandas as pd
import numpy as np
import ssl

# Temporary fix.  Don't do this in production code.
ssl._create_default_https_context = ssl._create_default_https_context

# show all columns and format floats as currency with 2 decimals
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', "${:,.2f}".format)

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

try:
    df = pd.read_csv(url, engine="pyarrow")
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')

    # ensure numeric before computing sales (coerce bad values to NaN)
    df['quantity'] = pd.to_numeric(df.get('quantity'), errors='coerce')
    df['unit_price'] = pd.to_numeric(df.get('unit_price'), errors='coerce')
    df['sales'] = df['quantity'].fillna(0) * df['unit_price'].fillna(0)

    # Create a pivot table aggregating sales by state and with sub-columns for
    # total (sum) and average (mean) per order_type/customer_type
    pivot_table = pd.pivot_table(
        df,
        values='sales',
        index='customer_state',
        columns=['customer_type', 'order_type'],
        aggfunc=[np.sum, np.mean],     # sub-columns: sum and mean (average)
        margins=True,
        margins_name='Total Sales'
    )

    print(pivot_table)

except Exception as e:
    print(f"Error reading CSV: {e}")