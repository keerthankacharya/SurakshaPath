from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from pathlib import Path

app = Flask(__name__)
CORS(app)

# Load data from local files
ALERTS_PATH = Path(__file__).parent / 'alerts.json'
NEWS_PATH = Path(__file__).parent / 'news.json'

# Load your data
with open(ALERTS_PATH, 'r') as f:
    alerts_data = json.load(f)

with open(NEWS_PATH, 'r') as f:
    news_data = json.load(f)

@app.route('/api/alerts', methods=['GET'])
def get_alerts():
    return jsonify(alerts_data.get('alerts', []))

@app.route('/api/news', methods=['GET'])
def get_news():
    return jsonify(news_data.get('news', []))

# Vercel serverless function handler
def handler(request):
    """Vercel serverless function handler"""
    return app(request) 