from django.shortcuts import render
import json
import os

def load_articles():
    with open(os.path.join(os.path.dirname(__file__), '../articles.json')) as f:
        return json.load(f)

def article_list(request):
    articles = load_articles()
    return render(request, 'article_list.html', {'articles': articles})

def article_detail(request, article_id):
    articles = load_articles()
    article = next((article for article in articles if article['id'] == article_id), None)
    return render(request, 'article_detail.html', {'article': article})