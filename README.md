<h1 align="center">REDDIT CONTENT ANALYSIS API</h1>
<p align="center"><em>FastAPI + Django hybrid for Reddit content analysis and intelligent post generation using LangGraph.</em></p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-async-green" alt="FastAPI">
  <img src="https://img.shields.io/badge/Django-admin-blue" alt="Django">
</p>
<br/>
<p align="center"><em>Build tools and technologies:</em></p>
<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/LangGraph-FF6B6B?style=for-the-badge" alt="LangGraph">
  <img src="https://img.shields.io/badge/TextBlob-4CAF50?style=for-the-badge" alt="TextBlob">
  <img src="https://img.shields.io/badge/Pydantic-E92063?style=for-the-badge&logo=pydantic&logoColor=white" alt="Pydantic">
  <img src="https://img.shields.io/badge/Uvicorn-FF4785?style=for-the-badge" alt="Uvicorn">
</p>

FastAPI + Django hybrid using LangGraph for intelligent Reddit content analysis and post generation.

## Features

- Text sentiment analysis with TextBlob
- AI-powered Reddit post generation
- Cached analysis results
- Django admin panel

## Quick Start

```bash
git clone git@github.com:preston-56/reddit-content-analysis.git
cd reddit-content-analysis
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py collectstatic
uvicorn fastapi_app.main:app --reload
```

## API Endpoints

```bash
POST /v1/analyze/   # Sentiment analysis
POST /v1/generate/  # Generate posts
GET  /v1/results/   # Get results
GET  /docs          # API docs
GET  /admin         # Admin panel
```

## API Playground

**Python Client:**
```python
import requests

# Generate Reddit post
response = requests.post("http://localhost:8000/v1/generate/",
    json={"subreddit": "python"})
print(response.json())

# Analyze text sentiment
response = requests.post("http://localhost:8000/v1/analyze/",
    json={"text": "FastAPI is amazing!"})
print(response.json())
```

**FastAPI Interactive Docs:**
```bash
# Start server and visit interactive API docs
uvicorn fastapi_app.main:app --reload
# Open http://localhost:8000/docs
```

**cURL Commands:**
```bash
# Generate post suggestion
curl -X POST "http://localhost:8000/v1/generate/" \
     -H "Content-Type: application/json" \
     -d '{"subreddit": "programming"}'

# Sentiment analysis
curl -X POST "http://localhost:8000/v1/analyze/" \
     -H "Content-Type: application/json" \
     -d '{"text": "This API rocks!"}'
```

## Tech Stack

FastAPI • Django • LangGraph • TextBlob • Pydantic • Uvicorn