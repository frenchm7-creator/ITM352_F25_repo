# Import required libraries for web framework, data processing, and visualization
from flask import Flask, render_template, request, session, flash, redirect, url_for
import pandas as pd
import matplotlib
matplotlib.use('Agg')  
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import IsolationForest  # Machine learning for anomaly detection
import os

# Initialize Flask application
app = Flask(__name__)
app.secret_key = "your-secret-key-here"

# Configure folder for saving charts
UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global variable to store uploaded dataframe across requests
current_df = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/process", methods=["POST"])
def process():
    """Process uploaded file and generate quality report"""
    global current_df
    try:
        # Get uploaded file from form
        file = request.files.get("file")
        if not file:
            flash("No file selected", "danger")
            return redirect(url_for("upload"))
        
        # Read file based on extension using pandas
        if file.filename.endswith(".csv"):
            current_df = pd.read_csv(file)
        elif file.filename.endswith(".xlsx"):
            current_df = pd.read_excel(file)
        else:
            flash("Invalid file format. Please upload CSV or XLSX", "danger")
            return redirect(url_for("upload"))
        
        # Calculate data quality statistics
        missing = current_df.isnull().sum().to_dict()  # Count missing values per column
        duplicates = int(current_df.duplicated().sum())  # Count duplicate rows
        total_rows = len(current_df)
        summary = current_df.describe(include="all").to_html(classes="table")
        
        # Calculate overall quality score (0-100)
        quality_score = calculate_quality_score(current_df)
        
        # Generate basic visualization chart
        chart_path = create_basic_chart(current_df)
        
        flash("File processed successfully!", "success")
        return render_template("results.html",
            missing=missing,
            duplicates=duplicates,
            total_rows=total_rows,
            quality_score=quality_score,
            summary=summary,
            chart=chart_path)
    
    except Exception as e:
        # Error handling 
        flash(f"Error processing file: {str(e)}", "danger")
        return redirect(url_for("upload"))

@app.route("/data_viewer")
def data_viewer():
    """Display first 50 rows of uploaded data"""
    global current_df
    if current_df is not None:
        # Convert first 50 rows to HTML table for display
        data_html = current_df.head(50).to_html(classes="table")
        return render_template("data_viewer.html", data=data_html)
    return render_template("data_viewer.html", data=None)

@app.route("/analysis")
def analysis():
    """Show advanced charts and statistical analysis"""
    global current_df
    if current_df is None:
        return render_template("analysis.html", charts=None, statistics=None)
    
    # Create multiple chart types (histogram, box plot)
    charts = create_analysis_charts(current_df)
    # Generate statistical summary table
    statistics = current_df.describe(include="all").to_html(classes="table")
    return render_template("analysis.html", charts=charts, statistics=statistics)

@app.route("/anomaly_detection")
def anomaly_detection():
    """Use machine learning to find unusual data points"""
    global current_df
    if current_df is None:
        return render_template("anomaly.html", anomalies=None, anomaly_chart=None)
    
    # Apply Isolation Forest algorithm to detect outliers
    anomalies_df, chart_path = detect_anomalies(current_df)
    anomalies_html = anomalies_df.to_html(classes="table") if anomalies_df is not None else None
    return render_template("anomaly.html", anomalies=anomalies_html, anomaly_chart=chart_path)

@app.route("/documentation")
def documentation():
    return render_template("documentation.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Helper functions for data analysis
def calculate_quality_score(df):
    """Calculate overall data quality score (0-100)"""
    # Count total cells and problems
    total_cells = df.size
    missing_cells = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()
    
    # Apply penalties: missing values (up to 40 points), duplicates (up to 30 points)
    missing_penalty = (missing_cells / total_cells) * 40
    duplicate_penalty = min((duplicate_rows / len(df)) * 30, 30)
    
    # Calculate final score (higher is better)
    score = max(0, 100 - missing_penalty - duplicate_penalty)
    return int(score)

def create_basic_chart(df):
    """Create a simple bar chart for numeric data"""
    # Find numeric columns in dataframe
    numeric_cols = df.select_dtypes(include=["number"]).columns
    if len(numeric_cols) > 0:
        plt.figure(figsize=(10, 6))
        col = numeric_cols[0]  # Use first numeric column
        # Plot first 10 values as bar chart
        df[col].head(10).plot(kind="bar", color="skyblue")
        plt.title(f"Distribution of {col}")
        plt.tight_layout()
        # Save chart to static folder
        path = os.path.join(UPLOAD_FOLDER, "chart_basic.png")
        plt.savefig(path)
        plt.close()  # Close figure to free memory
        return "chart_basic.png"
    return None

def create_analysis_charts(df):
    """Create multiple charts for analysis"""
    charts = {}
    numeric_cols = df.select_dtypes(include=["number"]).columns
    
    if len(numeric_cols) > 0:
        # Create histogram to show data distribution
        plt.figure(figsize=(10, 6))
        df[numeric_cols[0]].hist(bins=20, color="coral", edgecolor="black")
        plt.title(f"Histogram of {numeric_cols[0]}")
        plt.xlabel(numeric_cols[0])
        plt.ylabel("Frequency")
        path = os.path.join(UPLOAD_FOLDER, "chart_histogram.png")
        plt.savefig(path)
        plt.close()
        charts["Histogram"] = "chart_histogram.png"
        
        # Create box plot to identify outliers (if multiple numeric columns exist)
        if len(numeric_cols) >= 2:
            plt.figure(figsize=(10, 6))
            df[numeric_cols[:3]].boxplot()  # Show first 3 numeric columns
            plt.title("Box Plot of Numeric Columns")
            path = os.path.join(UPLOAD_FOLDER, "chart_boxplot.png")
            plt.savefig(path)
            plt.close()
            charts["Box Plot"] = "chart_boxplot.png"
    
    return charts if charts else None

def detect_anomalies(df):
    """Use Isolation Forest machine learning algorithm to detect anomalies"""
    # Keep only numeric columns and remove missing values
    numeric_df = df.select_dtypes(include=["number"]).dropna()
    
    # Need at least 10 rows for reliable anomaly detection
    if len(numeric_df) < 10 or numeric_df.shape[1] == 0:
        return None, None
    
    # Train Isolation Forest model (contamination=0.1 means expect 10% anomalies)
    iso_forest = IsolationForest(contamination=0.1, random_state=42)
    predictions = iso_forest.fit_predict(numeric_df)
    
    # Extract rows identified as anomalies (prediction = -1)
    anomalies = numeric_df[predictions == -1]
    
    # Create scatter plot visualization if anomalies found and 2+ numeric columns
    if len(anomalies) > 0 and numeric_df.shape[1] >= 2:
        plt.figure(figsize=(10, 6))
        cols = numeric_df.columns[:2]  # Use first 2 columns for x and y axes
        # Color code points: normal (yellow) vs anomaly (purple)
        plt.scatter(numeric_df[cols[0]], numeric_df[cols[1]], 
                   c=predictions, cmap="viridis", alpha=0.6)
        plt.xlabel(cols[0])
        plt.ylabel(cols[1])
        plt.title("Anomaly Detection (red = anomaly)")
        plt.colorbar(label="Normal (1) / Anomaly (-1)")
        path = os.path.join(UPLOAD_FOLDER, "chart_anomaly.png")
        plt.savefig(path)
        plt.close()
        return anomalies, "chart_anomaly.png"
    
    return anomalies if len(anomalies) > 0 else None, None

if __name__ == "__main__":
    app.run(debug=True)