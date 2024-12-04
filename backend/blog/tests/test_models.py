from django.test import TestCase
from blog.models import BlogCategory, BlogPost, Comment
from user.models import User


class BlogCategoryModelTest(TestCase):
    def test_category_str(self):
        category = BlogCategory.objects.create(name="Tech", slug="tech")
        self.assertEqual(str(category), "Tech")


class CommentModelTest(TestCase):
    def test_comment_creation(self):
        user = User.objects.create_user(username='testuser', password='password')
        category = BlogCategory.objects.create(name="Tech", slug="tech")
        post = BlogPost.objects.create(title="Sample Post", content="Content", category=category)
        comment = Comment.objects.create(content="Great post!", post=post, author=user)

        self.assertEqual(comment.content, "Great post!")
        self.assertEqual(comment.post.title, "Sample Post")
        self.assertEqual(comment.author.username, "testuser")
