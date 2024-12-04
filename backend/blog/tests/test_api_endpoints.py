from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import BlogPost, BlogCategory, Comment
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class CommentListCreateViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='password'
        )
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password'
        )
        self.post = BlogPost.objects.create(title='Test Post', content='Test content')
        self.url = reverse('comment-list-create', args=[self.post.pk])

    def get_auth_token(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

    def test_create_comment_as_admin(self):
        token = self.get_auth_token(self.admin)
        response = self.client.post(
            self.url,
            {'content': 'Test comment', 'post': self.post.id},  # 'post' instead of 'blog_post'
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        print(response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_comment_as_regular_user(self):
        token = self.get_auth_token(self.user)
        response = self.client.post(
            self.url,
            {'content': 'Test comment', 'post': self.post.id},  # 'post' instead of 'blog_post'
            format='json',
            HTTP_AUTHORIZATION=f'Bearer {token}'
        )
        print(response.data)  # Print response data for debugging
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_comment_without_authentication(self):
        response = self.client.post(self.url, {'content': 'Test comment', 'blog_post': self.post.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_comments_as_admin(self):
        token = self.get_auth_token(self.admin)
        Comment.objects.create(content='Test comment', post=self.post, author=self.admin)
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comments_as_regular_user(self):
        token = self.get_auth_token(self.user)
        Comment.objects.create(content='Test comment', post=self.post, author=self.user)
        response = self.client.get(self.url, HTTP_AUTHORIZATION=f'Bearer {token}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)



