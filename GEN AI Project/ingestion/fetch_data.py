import requests
from config.config import NEWS_API_KEY

def fetch_ai_news():
    url = f"https://newsapi.org/v2/everything?q=AI&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()

    articles = []
    for article in data["articles"][:10]:
        articles.append({
            "title": article["title"],
            "content": article["description"]
        })

    return articles