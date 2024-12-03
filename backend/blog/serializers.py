# serializers.py
from rest_framework import serializers
from .models import BlogCategory, BlogPost, Comment

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ['id', 'name', 'slug']

class BlogPostSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(queryset=BlogCategory.objects.all(), source='category', write_only=True)
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'category_id', 'image', 'time_to_read']

    def create(self, validated_data):
        category = validated_data.pop('category', None)
        post = BlogPost.objects.create(**validated_data, category=category)
        return post

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'post', 'author']
        read_only_fields = ['author']

