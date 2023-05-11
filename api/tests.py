from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
import json
from .models import Article

class ArticleTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
    #create article
    def test_create_article(self):
        url = reverse('articles')
        data = {
            "title": "test",
            "content": "test"
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
    #get articles list
    def test_get_list_articles(self):
        url = reverse('articles')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #get article detail
    def test_get_article_detail(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        url = reverse('article-detail', args=[article.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Article')

    #update article
    def test_update_article(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        url = reverse('article-detail', args=[article.pk])
        data = {
            "title": "Updated Article",
            "content": "Updated Content"
        }
        response = self.client.put(url, data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Article')

    #delete article
    def test_delete_article(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        url = reverse('article-detail', args=[article.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Article.objects.count(), 0)