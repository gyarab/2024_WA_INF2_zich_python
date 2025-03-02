from django.shortcuts import render, get_object_or_404
import json
import os

# Load articles data from JSON file
def load_articles():
    with open(os.path.join(os.path.dirname(__file__), '../..', 'articles.json'), 'r') as file:
        return json.load(file)

def index(request):
    articles = load_articles()
    return render(request, 'articles/index.html', {'articles': articles})

def detail(request, article_id):
    articles = load_articles()
    article = get_object_or_404(articles, id=article_id)
    return render(request, 'articles/detail.html', {'article': article})