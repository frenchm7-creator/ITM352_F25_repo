# Test Data Files

This folder contains sample inventory files for testing the Inventory Cleaner application.

## Files Included

1. **clean_data.csv** - Perfect data with no issues (10 rows)
2. **missing_values.csv** - Contains intentional missing values in various columns
3. **duplicates.csv** - Contains duplicate rows for testing duplicate detection
4. **outliers.csv** - Contains extreme values to test anomaly detection
5. **sample_inventory.csv** - Larger dataset (40 rows) with mixed issues

## Usage

Upload any of these files through the application's Upload page to test different features:

- Use **clean_data.csv** to verify the app works with valid data
- Use **missing_values.csv** to test missing value detection
- Use **duplicates.csv** to test duplicate detection
- Use **outliers.csv** to test anomaly detection
- Use **sample_inventory.csv** for comprehensive testing

## Expected Results

### clean_data.csv
- Quality Score: ~95-100%
- Missing Values: 0
- Duplicates: 0
- Anomalies: 0

### missing_values.csv
- Quality Score: ~40-60%
- Missing Values: 8-10 cells
- Should trigger low quality warnings

### duplicates.csv
- Quality Score: ~70-80%
- Duplicates: 3-4 rows
- Should show duplicate detection working

### outliers.csv
- Should detect 2-3 anomalies (expensive items)
- Anomaly detection algorithm should flag extreme prices
