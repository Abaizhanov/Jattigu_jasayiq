from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from blog.models import BlogPost, BlogCategory
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class BlogPostDetailViewTest(TestCase):

    def setUp(self):
        # Create an admin user with a unique email
        self.admin_user = User.objects.create_user(
            username='admin',
            email='admin@example.com',  # Ensure unique email
            password='password'
        )
        self.admin_user.is_staff = True  # Make the user an admin
        self.admin_user.save()

        # Create a regular user with a unique email
        self.regular_user = User.objects.create_user(
            username='regular',
            email='regular@example.com',  # Ensure unique email
            password='password'
        )

        # Create a category for the blog post
        self.category = BlogCategory.objects.create(name="Tech", slug="tech")

        # Create a blog post
        self.blog_post = BlogPost.objects.create(
            title="Sample Post",
            content="Content for the sample post",
            category=self.category
        )

        # Generate JWT tokens for authentication
        self.admin_token = str(RefreshToken.for_user(self.admin_user).access_token)
        self.regular_token = str(RefreshToken.for_user(self.regular_user).access_token)

        # Use APIClient instead of Client to support `credentials` method
        self.client = APIClient()

    def test_get_blog_post_as_admin(self):
        url = reverse('post-detail', kwargs={'pk': self.blog_post.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.blog_post.title)

    def test_get_blog_post_as_regular_user(self):
        url = reverse('post-detail', kwargs={'pk': self.blog_post.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.regular_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.blog_post.title)


    def test_delete_blog_post_as_admin(self):
        url = reverse('post-detail', kwargs={'pk': self.blog_post.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.admin_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(BlogPost.objects.filter(pk=self.blog_post.pk).exists())


class BlogCategoryListCreateViewTest(TestCase):

    def setUp(self):
        # Create an admin user with a unique email
        self.admin_user = User.objects.create_user(
            username='admin',
            email='admin@example.com',
            password='password'
        )
        self.admin_user.is_staff = True  # Ensure admin status
        self.admin_user.save()

        # Check if admin user is correctly set as staff
        print(f"Admin user is_staff: {self.admin_user.is_staff}")  # Debugging

        # Generate JWT token for admin user
        self.admin_token = str(RefreshToken.for_user(self.admin_user).access_token)

        # Use APIClient for API requests
        self.client = APIClient()


    def test_get_blog_categories_as_regular_user(self):
        # Test regular user access (should be denied)
        regular_user = User.objects.create_user(
            username='regular',
            email='regular@example.com',  # Ensure unique email
            password='password'
        )
        regular_token = str(RefreshToken.for_user(regular_user).access_token)

        url = reverse('category-list-create')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {regular_token}')
        response = self.client.get(url)

        # Regular user should not have access (403 Forbidden)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


