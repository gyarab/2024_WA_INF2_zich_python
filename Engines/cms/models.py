from django.db import models
import json
import os

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    @classmethod
    def load_articles(cls):
        json_file_path = os.path.join(os.path.dirname(__file__), '../articles.json')
        with open(json_file_path, 'r') as file:
            articles_data = json.load(file)
            for article in articles_data:
                cls.objects.create(
                    title=article['title'],
                    content=article['content'],
                    published_date=article['published_date']
                )