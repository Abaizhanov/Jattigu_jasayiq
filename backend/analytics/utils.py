# analytics/utils.py

from blog.models import BlogPost
from user.models import User
from datetime import datetime, timedelta
from django.db.models import Count

def get_blog_trends():
    # Получаем тренды блогов (например, посты с более чем 50 комментариями)
    blog_posts = BlogPost.objects.annotate(comment_count=Count('comment')).filter(comment_count__gte=50)
    
    blog_trends = [{"title": post.title, "comment_count": post.comment_count} for post in blog_posts]
    return blog_trends

def get_user_behavior():
    # Анализируем поведение пользователей (например, количество входов за последние 30 дней)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)
    user_logins = User.objects.filter(last_login__gte=start_date)

    user_behavior = [{"username": user.username, "logins": user_logins.filter(username=user.username).count()} for user in user_logins]
    return user_behavior
