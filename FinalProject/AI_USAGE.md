# How I Used AI in This Project

## Overview

This document explains exactly how I used AI tools (ChatGPT and GitHub Copilot) to build the Inventory Cleaner. I did NOT ask AI to build the whole program. Instead, I used AI to help with specific problems.

## What I Did Myself vs. What AI Helped With

### I Did These By Myself:
1. Decided what features the program should have
2. Designed the structure with 8 pages
3. Created the quality scoring formula
4. Organized all the files and folders
5. Tested everything thoroughly
6. Decided which technologies to use

### AI Helped Me With:
Technical problems that I got stuck on

---

## Specific Examples of AI Use

### 1. Error Handling for File Uploads

**The Problem**: I didn't know the best way to catch errors when users upload files.

**What I Asked AI**: "How do I handle file upload errors in Flask with try-catch blocks?"

**What AI Told Me**: 
- Use `try` and `except` blocks
- Check if file exists with `request.files.get()`
- Use Flask's `flash()` to show error messages

**What I Did**: 
- Took AI's advice
- Added try-except blocks around my file processing code
- Added checks for file format (.csv or .xlsx)
- Made error messages friendly for users

**Code Example**:
```python
try:
    file = request.files.get("file")
    if not file:
        flash("No file selected", "danger")
        return redirect(url_for("upload"))
except Exception as e:
    flash(f"Error: {str(e)}", "danger")
```

### 2. Machine Learning - Isolation Forest

**The Problem**: I knew I wanted to detect unusual data, but didn't know how to use Isolation Forest.

**What I Asked AI**: "How do I use Isolation Forest from scikit-learn to find outliers in data?"

**What AI Told Me**:
- Use `from sklearn.ensemble import IsolationForest`
- Set contamination parameter (how much data is unusual)
- Fit the model on numeric columns only
- Predictions of -1 mean unusual, 1 means normal

**What I Did**:
- Used AI's example as a starting point
- Changed it to work with my DataFrame
- Added error handling for when there's not enough data
- Set contamination=0.1 (expect 10% unusual items)

**Code Example**:
```python
iso_forest = IsolationForest(contamination=0.1, random_state=42)
predictions = iso_forest.fit_predict(numeric_df)
anomalies = numeric_df[predictions == -1]
```

**Why This Shows I Understand**: I knew what anomaly detection was from class, then used AI to learn the specific tool.

### 3. Matplotlib Backend Issue

**The Problem**: I got error "main thread is not in main loop" when creating charts.

**What I Asked AI**: "How to fix matplotlib threading error in Flask?"

**What AI Told Me**: Add `matplotlib.use('Agg')` before importing pyplot

**What I Did**: 
- Added that line to my app.py
- Tested to make sure it worked
- Applied the same fix to all my chart functions

**Code Example**:
```python
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
```

### 4. CSS Grid Layout

**The Problem**: I wanted my feature cards to arrange nicely on different screen sizes.

**What I Asked AI**: "CSS grid that shows 4 columns on big screens and 1 column on phones"

**What AI Told Me**: Use `grid-template-columns: repeat(auto-fit, minmax(250px, 1fr))`

**What I Did**:
- Used this in my .features-grid class
- Tested on different screen sizes
- Adjusted the 250px to fit my cards better

**CSS Example**:
```css
.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 1.5rem;
}
```

### 5. Pandas describe() Function

**The Problem**: My summary statistics only showed number columns, not text columns.

**What I Asked AI**: "How to make pandas describe() show all columns including text?"

**What AI Told Me**: Add `describe(include='all')`

**What I Did**: Changed `df.describe()` to `df.describe(include='all')` everywhere

### 6. Quality Score Formula

**The Problem**: I needed a formula to turn missing values and duplicates into a 0-100 score.

**What I Asked AI**: "How to calculate a data quality score from missing values and duplicates?"

**What AI Told Me**: Use a penalty system where missing data and duplicates reduce the score

**What I Did**: Created my own formula:
- Start at 100
- Subtract 40% for missing values
- Subtract 30% for duplicates
- Never go below 0

**Code I Wrote**:
```python
def calculate_quality_score(df):
    total_cells = df.size
    missing_cells = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    
    missing_penalty = (missing_cells / total_cells) * 40
    duplicate_penalty = min((duplicate_rows / len(df)) * 30, 30)
    
    score = max(0, 100 - missing_penalty - duplicate_penalty)
    return int(score)
```

**Why This is Original**: AI gave me the idea of penalties, but I decided the specific numbers myself.

### 7. Flask Routes Structure

**The Problem**: Wasn't sure how to organize multiple pages in Flask.

**What I Asked AI**: "How to create multiple pages in Flask with templates?"

**What AI Told Me**: 
- Use `@app.route()` for each page
- Create one base template
- Other templates extend the base

**What I Did**:
- Created 8 routes in app.py
- Made base.html with navigation
- Made all pages extend base.html

### 8. Session Storage

**The Problem**: Needed to remember the uploaded data across different pages.

**What I Asked AI**: "How to store data between Flask pages without a database?"

**What AI Told Me**: Can use global variable for simple single-user app

**What I Did**: Used global variable `current_df` to store the DataFrame

**Why This Shows Understanding**: I know this isn't perfect for production, but it works for a class project.

---

## Where AI Did NOT Help

These things I figured out myself:

1. **Deciding Quality Score Weights**: The 40% and 30% penalties came from my judgment
2. **Choosing 8 Pages**: I decided the site needed 8 different pages
3. **Test File Creation**: I created all 5 test files myself
4. **Color Scheme**: I picked the colors for the website
5. **Feature Selection**: I decided which features to include

---

## How ITM352 Knowledge Helped Me Use AI Better

Because I learned Pandas in class, I could:
- Ask specific questions about DataFrame operations
- Understand AI's code examples
- Modify AI suggestions to fit my needs

Because I learned Flask basics in class, I could:
- Ask the right questions about routing and templates
- Know when AI's answers didn't fit my project
- Debug when something didn't work

Because I learned about data analysis in class, I could:
- Understand what anomaly detection means
- Ask targeted questions about Isolation Forest
- Interpret the results correctly

---

## Conclusion

I used AI as a helper for specific technical problems, not as a tool to build the whole program. The project structure, feature selection, and overall design were my own work. AI saved me time on syntax and debugging, but the thinking and planning came from me.

**Time Estimate**:
- Without AI: Would have taken 8+ hours of reading documentation
- With AI: Took about 5 hours total
- AI helped me focus on learning concepts instead of memorizing syntax
