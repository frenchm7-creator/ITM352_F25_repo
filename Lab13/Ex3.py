from flask import Flask, render_template_string
import requests

app = Flask(__name__)
API_URL = "https://meme-api.com/gimme/wholesomememes"

HTML = """<!doctype html>
<html>
<head>
  <title>Memes'R'Us</title>
  <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=0.8">
  <meta http-equiv="refresh" content="10; url=http://127.0.0.1:5000" />
  <style>
    body { font-family: Arial, Helvetica, sans-serif; text-align: center; padding: 1rem; }
    img  { max-width: 90%; height: auto; border-radius: 6px; box-shadow: 0 2px 6px rgba(0,0,0,0.15); }
    .meta { margin-top: .5rem; color: #444; }
  </style>
</head>
<body>
  <h1>Memes'R'Us</h1>
  {% if error %}
    <p>Error: {{ error }}</p>
  {% else %}
    <a href="{{ post_link }}" target="_blank" rel="noopener">
      <img src="{{ url }}" alt="{{ title }}">
    </a>
    <div class="meta">r/{{ subreddit }} — <em>{{ title }}</em></div>
  {% endif %}
</body>
</html>
"""

@app.route("/")
def index():
    try:
        resp = requests.request("GET", API_URL, timeout=6)
        resp.raise_for_status()
        data = resp.json()
        return render_template_string(
            HTML,
            url=data.get("url"),
            subreddit=data.get("subreddit"),
            post_link=data.get("postLink", "#"),
            title=data.get("title", ""),
            error=None
        )
    except Exception as e:
        return render_template_string(HTML, error=str(e))

if __name__ == "__main__":
    app.run(debug=True)