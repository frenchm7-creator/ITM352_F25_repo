# Assignment 2. Build a Sales Dashboard
# Interactive text-based dashboard to analyze sales data
# using pandas pivot tables.
# The program loads sales data, checks for errors, provides summaries,
# and lets the user perform analytics through a simple menu.
# Name: Micah French
# Date: October 28, 2025

import pandas as pd
import time
import sys
import os


# Loads the CSV file, fills missing values with 0, and shows data summary.
def load_sales_data():
    print("\n--- Load Sales Data ---")
    print("1. Default file: sales_data.csv")
    print("2. Enter a custom file path")
    choice = input("Select an option (1 or 2): ")

    # Let user choose file
    if choice == "2":
        filepath = input("Enter the CSV file path: ").strip()
    else:
        filepath = "sales_data.csv"

    # Show loading indicator
    print("\nLoading sales data...")
    start_time = time.time()

    # Try to read file safely
    try:
        data = pd.read_csv(filepath)
    except FileNotFoundError:
        print("Error: File not found. Please check and try again.")
        sys.exit()
    except Exception as e:
        print("Error loading file:", e)
        sys.exit()

    end_time = time.time()
    print(f"File loaded successfully in {end_time - start_time:.2f} seconds.\n")

    # Replace missing values with 0
    data.fillna(0, inplace=True)

    # Display number of rows and columns
    print(f"Rows: {len(data)}, Columns: {len(data.columns)}\n")

    # Show column names
    print("Available columns:")
    for col in data.columns:
        print("-", col)

    # Check for required fields
    required_columns = [
        "order_number", "employee_id", "employee_name",
        "sales_region", "order_date", "order_type",
        "customer_type", "customer_state", "product_category",
        "quantity", "unit_price"
    ]

    missing = [c for c in required_columns if c not in data.columns]
    if missing:
        print("\nWarning: Missing columns detected:", missing)
        print("Some analytics may not work correctly.\n")

    # Add calculated column for total sale price
    data["sale_price"] = data["quantity"] * data["unit_price"]

    # Display a data summary
    print("\n--- Data Summary ---")
    try:
        print("Total Orders:", data["order_number"].nunique())
        print("Unique Employees:", data["employee_id"].nunique())
        print("Sales Regions:", data["sales_region"].nunique())
        print("Date Range:", data["order_date"].min(), "to", data["order_date"].max())
        print("Unique Customers:", data["customer_name"].nunique())
        print("Product Categories:", data["product_category"].nunique())
        print("Unique States:", data["customer_state"].nunique())
        print("Total Sales Amount:", round(data["sale_price"].sum(), 2))
        print("Total Quantity Sold:", data["quantity"].sum())
    except Exception as e:
        print("Some summary details could not be displayed:", e)

    print("\nData is ready for analysis.\n")
    return data

# Asks user if they want to export result to Excel file.
def export_result_to_excel(result):
    choice = input("Would you like to export this result to Excel? (y/n): ").lower()
    if choice == "y":
        filename = input("Enter a file name (without extension): ").strip()
        if filename == "":
            filename = "exported_result"
        result.to_excel(filename + ".xlsx")
        print("File saved as", filename + ".xlsx\n")


# Shows first N rows of data or all if requested.
def show_first_n_rows(data):
    total = len(data)
    print(f"\nEnter rows to display (1 to {total}), or 'all' for all rows.")
    print("Press Enter to skip.")
    choice = input("Your choice: ")

    if choice == "":
        print("No rows displayed.\n")
        return
    elif choice.lower() == "all":
        print(data)
    else:
        try:
            n = int(choice)
            if 1 <= n <= total:
                print(data.head(n))
            else:
                print("Invalid number of rows.\n")
        except:
            print("Invalid input.\n")



# Creates a pivot table safely using try/except.
def safe_pivot(data, index, columns, values, aggfunc):
    try:
        table = pd.pivot_table(data, index=index, columns=columns,
                               values=values, aggfunc=aggfunc, fill_value=0)
        print("\n", table)
        export_result_to_excel(table)
        return table
    except Exception as e:
        print("Error creating pivot table:", e)
        return None


# Analytic Functions
def total_sales_by_region_order_type(data):
    print("\n--- Total Sales by Region and Order Type ---")
    return safe_pivot(data, "sales_region", "order_type", "sale_price", "sum")


def avg_sales_by_region_state_type(data):
    print("\n--- Average Sales by Region, State, and Sale Type ---")
    return safe_pivot(data, ["sales_region", "customer_state"], "order_type", "sale_price", "mean")


def sales_by_customer_order_state(data):
    print("\n--- Sales by Customer Type and Order Type by State ---")
    return safe_pivot(data, "customer_state", ["customer_type", "order_type"], "sale_price", "sum")


def total_sales_qty_price_region_product(data):
    print("\n--- Total Sales Quantity and Price by Region and Product ---")
    return safe_pivot(data, "sales_region", "product_category", ["quantity", "sale_price"], "sum")


def total_sales_qty_price_customer_type(data):
    print("\n--- Total Sales Quantity and Price by Customer Type ---")
    return safe_pivot(data, "customer_type", "order_type", ["quantity", "sale_price"], "sum")


def max_min_sales_price_by_category(data):
    print("\n--- Max and Min Sales Price by Category ---")
    return safe_pivot(data, "product_category", None, "sale_price", ["max", "min"])


def unique_employees_by_region(data):
    print("\n--- Unique Employees by Region ---")
    result = data.groupby("sales_region")["employee_id"].nunique()
    print(result)
    export_result_to_excel(result)
    return result


# Allows user to create their own pivot table.
def custom_pivot_generator(data):
    print("\n--- Custom Pivot Table ---")

    # Show available columns
    print("\nAvailable columns for rows:")
    for i, col in enumerate(data.columns, 1):
        print(f"{i}. {col}")
    row_input = input("Enter row number(s), separated by commas: ")
    rows = []
    for i in row_input.split(","):
        if i.strip().isdigit():
            idx = int(i.strip()) - 1
            if 0 <= idx < len(data.columns):
                rows.append(data.columns[idx])

    # Choose columns
    print("\nAvailable columns for columns (optional):")
    for i, col in enumerate(data.columns, 1):
        print(f"{i}. {col}")
    col_input = input("Enter column number(s), or press Enter for none: ")
    cols = []
    if col_input.strip() != "":
        for i in col_input.split(","):
            if i.strip().isdigit():
                idx = int(i.strip()) - 1
                if 0 <= idx < len(data.columns):
                    cols.append(data.columns[idx])
    if len(cols) == 0:
        cols = None

    # Choose numeric fields
    numeric_fields = ["quantity", "unit_price", "sale_price"]
    print("\nAvailable numeric fields for values:")
    for i, col in enumerate(numeric_fields, 1):
        print(f"{i}. {col}")
    val_input = input("Enter number(s) separated by commas: ")
    values = []
    for i in val_input.split(","):
        if i.strip().isdigit():
            idx = int(i.strip()) - 1
            if 0 <= idx < len(numeric_fields):
                values.append(numeric_fields[idx])

    # Choose aggregation function
    print("\nChoose aggregation function:")
    print("1. sum")
    print("2. mean")
    print("3. count")
    agg_choice = input("Enter your choice (1-3): ")
    if agg_choice == "2":
        aggfunc = "mean"
    elif agg_choice == "3":
        aggfunc = "count"
    else:
        aggfunc = "sum"

    return safe_pivot(data, rows, cols, values, aggfunc)


# Lets user compare two analytics side by side.
def compare_two_analytics(data):
    print("\n--- Compare Two Analytics ---")
    print("First analytic:")
    first = total_sales_by_region_order_type(data)

    print("\nSecond analytic:")
    second = total_sales_qty_price_region_product(data)

    print("\n--- Comparison (Side by Side) ---")
    try:
        combined = pd.concat([first, second], axis=1)
        print(combined)
        export_result_to_excel(combined)
    except:
        print("Unable to combine results.")


# Displays the main dashboard menu.
def main_menu(data):
    menu_items = [
        ("Show first n rows", show_first_n_rows),
        ("Total sales by region and order_type", total_sales_by_region_order_type),
        ("Average sales by region/state/sale type", avg_sales_by_region_state_type),
        ("Sales by customer/order type by state", sales_by_customer_order_state),
        ("Total sales qty & price by region/product", total_sales_qty_price_region_product),
        ("Total sales qty & price by customer type", total_sales_qty_price_customer_type),
        ("Max and min sales price by category", max_min_sales_price_by_category),
        ("Unique employees by region", unique_employees_by_region),
        ("Create custom pivot table", custom_pivot_generator),
        ("Compare two analytics", compare_two_analytics)
    ]

    while True:
        print("\n--- Sales Data Dashboard ---")
        for i, (label, _) in enumerate(menu_items, 1):
            print(f"{i}. {label}")
        print(f"{len(menu_items) + 1}. Exit")

        choice = input("\nEnter your choice: ")

        try:
            choice = int(choice)
            if 1 <= choice <= len(menu_items):
                menu_items[choice - 1][1](data)
            elif choice == len(menu_items) + 1:
                print("\nExiting Sales Dashboard. Goodbye!")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Please enter a valid number.")


# Start the main program
if __name__ == "__main__":
    print("Welcome to the Sales Dashboard!")
    sales_data = load_sales_data()
    main_menu(sales_data)