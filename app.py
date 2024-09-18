# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello():
#     return "Hello, Terraform!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=80)

from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def get_top_animes():
    url = "https://api.jikan.moe/v4/top/anime?limit=25"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        top_animes = []
        for anime in data['data']:
            top_animes.append({
                "title": anime['title'],
                "rank": anime['rank'],
                "score": anime['score'],
                "image_url": anime['images']['jpg']['image_url']  # Getting the image URL
            })
        
        # Render the HTML with data
        return render_template_string(html_template, top_animes=top_animes)
    else:
        return "Failed to fetch data from the API", response.status_code

# HTML Template with CSS styling for a neat format
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Top 100 Animes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
            margin-bottom: 40px;
        }
        .anime-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
        }
        .anime-card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            text-align: center;
        }
        .anime-card img {
            max-width: 100%;
            border-radius: 8px;
        }
        .anime-title {
            font-size: 18px;
            font-weight: bold;
            margin: 10px 0;
        }
        .anime-rank {
            color: #888;
            margin-bottom: 10px;
        }
        .anime-score {
            background-color: #ffdd57;
            padding: 5px 10px;
            border-radius: 20px;
            display: inline-block;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <h1>Top 100 Animes</h1>
    <div class="anime-container">
        {% for anime in top_animes %}
        <div class="anime-card">
            <img src="{{ anime.image_url }}" alt="{{ anime.title }}">
            <div class="anime-title">{{ anime.title }}</div>
            <div class="anime-rank">Rank: {{ anime.rank }}</div>
            <div class="anime-score">Score: {{ anime.score }}</div>
        </div>
        {% endfor %}
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
