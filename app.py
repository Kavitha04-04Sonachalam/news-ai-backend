from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # Fixes the CORS issue between frontend and backend

API_KEY = "e16ab92fe92f40a79194df2432b122e9"

@app.route('/news', methods=['POST'])
def get_news():
    data = request.get_json()
    topic = data.get("topic", "general")
    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={API_KEY}"

    try:
        response = requests.get(url)
        articles = response.json().get("articles", [])[:5]
        news = [article["title"] for article in articles]
        return jsonify({"news": news})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
