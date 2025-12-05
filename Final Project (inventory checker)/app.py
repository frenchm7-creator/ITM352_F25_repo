from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

UPLOAD_FOLDER = "static"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file = request.files["file"]

    # read file
    df = pd.read_csv(file) if file.filename.endswith(".csv") else pd.read_excel(file)

    # basic checks
    missing = df.isnull().sum().to_dict()
    duplicates = df.duplicated().sum()
    summary = df.describe(include="all").to_html()

    # simple chart (first numeric column)
    numeric_cols = df.select_dtypes(include="number").columns

    chart_path = None
    if len(numeric_cols) > 0:
        col = numeric_cols[0]
        plt.figure()
        df[col].head(10).plot(kind="bar")
        chart_path = os.path.join(UPLOAD_FOLDER, "chart.png")
        plt.savefig(chart_path)
        plt.close()

    return render_template(
        "results.html",
        missing=missing,
        duplicates=duplicates,
        summary=summary,
        chart="chart.png" if chart_path else None
    )

if __name__ == "__main__":
    app.run(debug=True)
