# urls.py
from django.urls import path
from .views import (
    BlogCategoryListCreateView,
    BlogPostCategoryView,
    # BlogCategoryDetailView,
    BlogPostListCreateView,
    BlogPostDetailView,
    CommentListCreateView,
)

urlpatterns = [
    path('categories/', BlogCategoryListCreateView.as_view(), name='category-list-create'),
    # path('categories/<slug:slug>/', BlogCategoryDetailView.as_view(), name='category-detail'),
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('posts/categories/<slug:slug>/', BlogPostCategoryView.as_view(), name='blogposts-by-category'),
    path('posts/<int:pk>/comments', CommentListCreateView.as_view(), name='comment-list-create'),
    path('posts/categories/<slug:slug>/', BlogPostCategoryView.as_view(), name='blogposts-by-category'),

]
