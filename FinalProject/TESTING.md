# Testing Plan and Results

## Testing Overview

This document shows all the tests I did to make sure the Inventory Cleaner works correctly.

## Test Files Used

I created 5 different test files in the `test_data/` folder:

1. **clean_data.csv** - Perfect data with no errors
2. **missing_values.csv** - Has empty cells
3. **duplicates.csv** - Has duplicate rows
4. **outliers.csv** - Has very high/low prices
5. **sample_inventory.csv** - Has multiple types of problems

## Tests Performed

### Test 1: Upload Valid CSV File
**What I Did**: Uploaded `clean_data.csv`  
**Expected**: File should upload and show results  
**Result**: PASS - File uploaded successfully and showed 10 items

### Test 2: Upload Excel File
**What I Did**: Uploaded an .xlsx file  
**Expected**: File should work just like CSV  
**Result**: PASS - Excel files work correctly

### Test 3: Upload Wrong File Type
**What I Did**: Tried to upload a .txt file  
**Expected**: Should show error message  
**Result**: PASS - Got error message "Invalid file format"

### Test 4: Missing Values Detection
**What I Did**: Uploaded `missing_values.csv` (has 8 empty cells)  
**Expected**: Should count all missing values  
**Result**: PASS - Found all 8 missing values correctly

### Test 5: Duplicate Detection
**What I Did**: Uploaded `duplicates.csv` (has 3 duplicate rows)  
**Expected**: Should count duplicate rows  
**Result**: PASS - Found 3 duplicates correctly

### Test 6: Quality Score Calculation
**What I Did**: Uploaded files with different quality levels  
**Expected**: Clean file gets high score, messy file gets low score  
**Result**: PASS  
- clean_data.csv = 95% quality  
- missing_values.csv = 52% quality  
- sample_inventory.csv = 78% quality

### Test 7: Chart Generation
**What I Did**: Uploaded file and checked if charts appear  
**Expected**: Should see bar chart on results page  
**Result**: PASS - Chart shows correctly

### Test 8: Multiple Chart Types
**What I Did**: Went to Analysis page after uploading  
**Expected**: Should see histogram and box plot  
**Result**: PASS - Both charts display correctly

### Test 9: Anomaly Detection
**What I Did**: Uploaded `outliers.csv` (has very expensive items)  
**Expected**: Should flag expensive items as unusual  
**Result**: PASS - Found 3 anomalies (items over $10,000)

### Test 10: Data Viewer Page
**What I Did**: Clicked "Data Viewer" after uploading  
**Expected**: Should show my data in a table  
**Result**: PASS - Table displays first 50 rows

### Test 11: Navigation Between Pages
**What I Did**: Clicked each link in the navigation menu  
**Expected**: All pages should load without errors  
**Result**: PASS - All 8 pages work correctly

### Test 12: No File Uploaded
**What I Did**: Went to Analysis page without uploading anything  
**Expected**: Should show message asking to upload file  
**Result**: PASS - Shows "No data available. Please upload file"

### Test 13: Empty File
**What I Did**: Uploaded an empty CSV file  
**Expected**: Should handle gracefully, not crash  
**Result**: PASS - Shows error message

### Test 14: Very Large File
**What I Did**: Uploaded file with 1000 rows  
**Expected**: Should process without crashing  
**Result**: PASS - Processed successfully in 3 seconds

### Test 15: File with Only Text
**What I Did**: Uploaded file with no numbers  
**Expected**: Charts should not crash  
**Result**: PASS - Shows message "No numeric data for charts"



## Test Results Summary

- **Total Tests**: 15
- **Passed**: 15
- **Failed**: 0
- **Success Rate**: 100%

## Conclusion

All features work as expected. The program correctly:
- Uploads and reads files
- Finds missing values and duplicates
- Calculates quality scores
- Creates charts
- Detects anomalies using machine learning
- Handles errors properly
- Works across all pages
