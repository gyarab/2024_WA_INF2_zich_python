from django.shortcuts import render, get_object_or_404
import json
import os

def load_data():
    with open(os.path.join(os.path.dirname(__file__), 'data.json')) as f:
        return json.load(f)

def home(request):
    articles = load_data()
    return render(request, 'home.html', {'articles': articles})

def detail(request, article_id):
    articles = load_data()
    article = get_object_or_404(articles, id=article_id)
    return render(request, 'detail.html', {'article': article})