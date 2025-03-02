from django.test import TestCase
from .models import Article

class ArticleModelTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article.",
            published_date="2024-01-01"
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.content, "This is a test article.")
        self.assertIsNotNone(self.article.published_date)

    def test_article_str(self):
        self.assertEqual(str(self.article), "Test Article")