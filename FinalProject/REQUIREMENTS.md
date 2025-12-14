# Technical Requirements - How I Met Them

## Assignment Requirements Checklist

This document shows how my Inventory Cleaner project meets all the assignment requirements.

---

## 1. Originality and Creativity

**Requirement**: Project must be original, not copied from online, and not built entirely by AI

**How I Met This**:
- Created a unique combination of features (data validation + ML + quality scoring)
- Searched online and found no complete app like mine
- Tested with AI - it could not build this full app
- Designed 8 pages and overall structure myself

**Evidence**: See PROPOSAL.md section 5

---

## 2. Technical Requirements

### Inputs and Outputs

**Requirement**: Include user input and meaningful output

**How I Met This**:
- **Input**: File upload form (CSV or Excel files)
- **Output**: Quality reports, charts, tables, statistics, anomaly lists

**Where in Code**: 
- Input: `templates/upload.html` (line 10)
- Output: `templates/results.html`, `templates/analysis.html`

### Logic and Functions

**Requirement**: Break program into functions

**How I Met This**: Created 4 main functions:

1. `calculate_quality_score(df)` - Lines 80-90 in app.py
2. `create_basic_chart(df)` - Lines 92-105 in app.py  
3. `create_analysis_charts(df)` - Lines 107-135 in app.py
4. `detect_anomalies(df)` - Lines 137-165 in app.py

Plus 8 route functions for each page.

### Data Types

**Requirement**: Use lists, dictionaries, or complex data types

**How I Met This**:
- **DataFrames**: Main data structure (Pandas DataFrame)
- **Dictionaries**: Store missing values `missing = df.isnull().sum().to_dict()`
- **Lists**: Numeric columns `numeric_cols = df.select_dtypes(include=["number"]).columns`
- **Arrays**: Used in anomaly detection calculations

**Where in Code**: Throughout app.py, especially lines 30-70

### Error Handling

**Requirement**: Handle errors properly

**How I Met This**:
- Try-catch blocks around file processing (line 25 in app.py)
- Check if file exists before processing
- Check file format (.csv or .xlsx only)
- Handle empty/corrupted files
- Show friendly error messages with Flask flash()

**Where in Code**: Lines 25-45 in app.py

### Class Topics (Need at least 2)

**Requirement**: Use major topics from class

**How I Met This**:

1. **Pandas** (Data Analysis)
   - Read files: `pd.read_csv()`, `pd.read_excel()`
   - Check missing: `df.isnull().sum()`
   - Check duplicates: `df.duplicated().sum()`
   - Statistics: `df.describe()`

2. **Matplotlib** (Charts)
   - Bar chart: Line 98 in app.py
   - Histogram: Line 115 in app.py
   - Box plot: Line 125 in app.py

3. **File I/O** (Reading Files)
   - CSV reading: Line 32 in app.py
   - Excel reading: Line 34 in app.py

4. **Flask** (Web Application)
   - 8 routes/pages
   - Templates with Jinja2
   - Form handling
   - Session management

### Stretch Goal

**Requirement**: Use something not taught in class

**How I Met This**: 
- **Machine Learning - Isolation Forest**
- Used scikit-learn library
- Implemented anomaly detection algorithm
- Can identify unusual data points automatically

**Where in Code**: Lines 137-165 in app.py (detect_anomalies function)

---

## 3. Good MIS Project Management

### Documentation

**Requirement**: Write clear documentation

**How I Met This**:
- PROPOSAL.md - Explains purpose and plan
- README.md - Installation and usage instructions
- TESTING.md - Testing plan and results
- AI_USAGE.md - Detailed AI use explanation
- Comments in code explaining key parts

### Testing Plan

**Requirement**: Demonstrate program works as intended

**How I Met This**:
- Created 5 test files in test_data/ folder
- Ran 15 different tests
- All tests passed
- Documented results in TESTING.md

---

## 4. Polished Final Product

### Well-Structured Code

**Requirement**: Organized and readable code

**How I Met This**:
- Functions are under 50 lines each
- Clear function names
- Organized into logical sections
- Comments explain complex parts
- app.py is only 180 lines total

### Logically Organized

**Requirement**: Makes sense and easy to follow

**How I Met This**:
- 8 pages with clear navigation
- Each page has one purpose
- Flow makes sense: Upload → Results → Analysis
- Folders organized: templates/, static/, test_data/

### Well-Tested

**Requirement**: Thorough testing

**How I Met This**:
- 15 test cases completed
- Tested with different file types
- Tested error scenarios
- All features verified working
- See TESTING.md for details

### Robust to Errors

**Requirement**: Handles user mistakes

**How I Met This**:
- Wrong file type → Shows error message
- No file selected → Shows error message
- Empty file → Handles gracefully
- No numeric data → Shows appropriate message
- Corrupted file → Catches error and informs user

### User-Friendly

**Requirement**: Easy to use

**How I Met This**:
- Clear navigation menu
- Simple upload form
- Easy-to-read results
- Professional styling
- Help text on each page

---

## Requirements Summary

| Requirement | Status | Evidence |
|------------|--------|----------|
| Original Idea | ✓ Met | PROPOSAL.md |
| User Input/Output | ✓ Met | File upload + multiple outputs |
| Functions | ✓ Met | 4 analysis functions + 8 routes |
| Data Types | ✓ Met | DataFrames, dicts, lists, arrays |
| Error Handling | ✓ Met | Try-catch + validation |
| Pandas | ✓ Met | Used throughout app.py |
| Charts | ✓ Met | 3 chart types with Matplotlib |
| File I/O | ✓ Met | Reads CSV and Excel |
| Web App | ✓ Met | Flask with 8 pages |
| Stretch Goal (ML) | ✓ Met | Isolation Forest algorithm |
| Documentation | ✓ Met | 4 markdown files + README |
| Testing | ✓ Met | 15 tests, all passed |
| Code Quality | ✓ Met | Clean, organized, commented |
| User-Friendly | ✓ Met | Professional UI, clear nav |
| Error Robust | ✓ Met | Handles all error cases |

---

## Conclusion

All requirements have been met. The project demonstrates:
- Original thinking and creativity
- Technical skills from ITM352
- Proper use of AI as a helper tool
- Good project management
- Professional final product
