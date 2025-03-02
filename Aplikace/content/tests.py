from django.test import TestCase
from .models import Article  # Assuming you have an Article model defined in models.py
import json
from django.core.files import File
from django.core.management import call_command

class ArticleModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Load data from JSON file
        with open('content/data.json') as f:
            data = json.load(f)
            for article in data:
                Article.objects.create(
                    title=article['title'],
                    content=article['content'],
                    author=article['author']
                )

    def test_article_creation(self):
        article = Article.objects.get(id=1)
        self.assertEqual(article.title, 'Sample Article Title')  # Replace with actual title from your JSON
        self.assertEqual(article.author, 'Author Name')  # Replace with actual author from your JSON

    def test_article_str(self):
        article = Article.objects.get(id=1)
        self.assertEqual(str(article), article.title)

    def test_article_content(self):
        article = Article.objects.get(id=1)
        self.assertTrue(len(article.content) > 0)  # Ensure content is not empty

    def test_homepage_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_detail_view(self):
        article = Article.objects.get(id=1)
        response = self.client.get(f'/articles/{article.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detail.html')