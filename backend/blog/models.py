from django.db import models
from django.utils.text import Truncator
from user.models import User

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('BlogCategory', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)  # Image field
    time_to_read = models.PositiveIntegerField(null=True, blank=True)  # Time to read in minutes

    def calculate_time_to_read(self):
        """Estimate time to read based on the word count of the content."""
        word_count = len(self.content.split())
        average_reading_speed = 200  # Average reading speed in words per minute
        return max(1, word_count // average_reading_speed)

    def save(self, *args, **kwargs):
        self.time_to_read = self.calculate_time_to_read()
        super().save(*args, **kwargs)

    def __str__(self):
        return Truncator(self.title).chars(50)  
    



class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)