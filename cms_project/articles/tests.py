from django.test import TestCase
from .models import Article
import json
from django.core.files import File

class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        with open('articles.json') as json_file:
            data = json.load(json_file)
            for article in data:
                Article.objects.create(
                    title=article['title'],
                    content=article['content'],
                    publication_date=article['publication_date']
                )

    def test_article_content(self):
        article = Article.objects.get(id=1)
        expected_object_name = f'{article.title}'
        self.assertEqual(expected_object_name, 'First Article Title')  # Replace with actual title

    def test_article_str(self):
        article = Article.objects.get(id=1)
        self.assertEqual(str(article), article.title)