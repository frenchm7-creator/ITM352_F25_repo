# Inventory Cleaner

## What This Program Does

This program helps you check and clean inventory data from CSV or Excel files. It automatically finds:
- Missing values (empty cells)
- Duplicate rows
- Unusual numbers that might be errors

**ITM352 Capstone Project - Fall 2025**

## Main Features
- Upload CSV or Excel files
- Find missing values
- Find duplicate rows
- Give data a quality score (0-100)
- Show charts (bar chart, histogram, box plot)
- Detect unusual items using machine learning
- 8 different web pages with easy navigation

## How It Works

1. You upload your CSV or Excel file
2. Program checks the data
3. You see results: quality score, missing values, duplicates
4. You can view charts and unusual items

## Technologies Used
- **Python** - Programming language
- **Flask** - Makes the website work
- **Pandas** - Works with data
- **Matplotlib** - Creates charts
- **Scikit-learn** - Machine learning for anomaly detection

## How to Run This Program

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Run the program:
```bash
python app.py
```

3. Open your web browser and go to:
```
http://127.0.0.1:5000
```

## How to Use

1. Click "Upload" in the menu
2. Choose your CSV or Excel file
3. Click "Process File"
4. Look at the results page
5. Click other menu items to see charts and more information

## Project Structure
```
inventory-cleaner/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── TESTING.md                  # Testing plan and results
├── AI_USAGE.md                 # AI usage documentation
├── REQUIREMENTS.md             # Requirements checklist
├── static/
│   ├── style.css              # Professional styling
│   └── *.png                  # Generated charts
├── templates/
│   ├── base.html              # Base template with navigation
│   ├── index.html             # Home page
│   ├── upload.html            # File upload page
│   ├── results.html           # Results display
│   ├── data_viewer.html       # Data table viewer
│   ├── analysis.html          # Advanced analysis
│   ├── anomaly.html           # Anomaly detection
│   ├── documentation.html     # User guide
│   └── about.html             # Project information
└── test_data/
    ├── clean_data.csv         # Perfect data for testing
    ├── missing_values.csv     # Data with missing values
    ├── duplicates.csv         # Data with duplicates
    ├── outliers.csv           # Data with extreme values
    ├── sample_inventory.csv   # Comprehensive test data
    └── README.md              # Test data documentation
```

## Test Files

The `test_data/` folder has 5 sample files you can try:
- **clean_data.csv** - Perfect data, no errors
- **missing_values.csv** - Has empty cells
- **duplicates.csv** - Has duplicate rows
- **outliers.csv** - Has very high/low prices
- **sample_inventory.csv** - Mix of different problems

## Documentation Files

- **PROPOSAL.md** - Original project proposal
- **TESTING.md** - All tests performed and results
- **AI_USAGE.md** - How I used AI to help build this
- **REQUIREMENTS.md** - How I met all assignment requirements

## Author
ITM352 Student - Fall 2025