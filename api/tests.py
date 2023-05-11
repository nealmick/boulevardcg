import json
from .models import Article
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

class ArticleTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
    #authenticate test client with token
    def get_authenticated_client(self):
        self.client.force_authenticate(user=self.user, token=self.token)
        return self.client

    # create article
    def test_create_article(self):
        url = reverse('articles')
        data = {
            "title": "test",
            "content": "test"
        }

        response = self.get_authenticated_client().post(
            url,
            data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.count(), 1)
    
    # get articles list
    def test_get_list_articles(self):
        url = reverse('articles')
        response = self.get_authenticated_client().get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # get article detail
    def test_get_article_detail(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        url = reverse('article-detail', args=[article.pk])
        response = self.get_authenticated_client().get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Article')

    # update article
    def test_update_article(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        url = reverse('article-detail', args=[article.pk])
        data = {
            "title": "Updated Article",
            "content": "Updated Content"
        }
        response = self.get_authenticated_client().put(
            url,
            data=json.dumps(data),
            content_type='application/json',
            HTTP_AUTHORIZATION='Token ' + self.token.key
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Article')

    # delete article
    def test_delete_article(self):
        article = Article.objects.create(title='Test Article', content='Test Content')
        url = reverse('article-detail', args=[article.pk])
        response = self.get_authenticated_client().delete(url, HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Article.objects.count(), 0)
