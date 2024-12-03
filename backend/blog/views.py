import logging
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import BlogCategory, BlogPost, Comment
from .serializers import BlogCategorySerializer, BlogPostSerializer, CommentSerializer
from user.permissions import IsAdminUser, IsRegularUser

logger = logging.getLogger('blog')  # Initialize logger for blog

# Для работы с категориями
class BlogCategoryListCreateView(generics.ListCreateAPIView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # Только для аутентифицированных администраторов

    @swagger_auto_schema(
        operation_description="Retrieve all blog categories or create a new one",
        responses={200: BlogCategorySerializer(many=True), 201: BlogCategorySerializer()},
        tags=['Blog Categories']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new blog category",
        request_body=BlogCategorySerializer,
        responses={201: BlogCategorySerializer()},
        tags=['Blog Categories']
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        logger.info(f"Creating a new blog category: {serializer.validated_data}")
        serializer.save()
        logger.info("Blog category successfully created")

# Для работы с постами по категориям
class BlogPostCategoryView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsRegularUser]

    @swagger_auto_schema(
        operation_description="Retrieve all blog posts for a specific category",
        responses={200: BlogPostSerializer(many=True)},
        tags=['Blog Posts']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        slug = self.kwargs['slug']
        logger.info(f"Fetching blog posts for category with slug: {slug}")
        return BlogPost.objects.filter(category__slug=slug)

# Для работы с постами
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    @swagger_auto_schema(
        operation_description="Retrieve all blog posts or create a new one",
        responses={200: BlogPostSerializer(many=True), 201: BlogPostSerializer()},
        tags=['Blog Posts']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new blog post",
        request_body=BlogPostSerializer,
        responses={201: BlogPostSerializer()},
        tags=['Blog Posts']
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        logger.info(f"Creating a new blog post: {serializer.validated_data}")
        serializer.save()
        logger.info("Blog post successfully created")

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsRegularUser]

    @swagger_auto_schema(
        operation_description="Retrieve a blog post by ID",
        responses={200: BlogPostSerializer()},
        tags=['Blog Posts']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a blog post by ID",
        request_body=BlogPostSerializer,
        responses={200: BlogPostSerializer()},
        tags=['Blog Posts']
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a blog post by ID",
        responses={204: "No Content"},
        tags=['Blog Posts']
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Для работы с комментариями
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser | IsRegularUser]

    @swagger_auto_schema(
        operation_description="Retrieve all comments or create a new one",
        responses={200: CommentSerializer(many=True), 201: CommentSerializer()},
        tags=['Comments']
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new comment",
        request_body=CommentSerializer,
        responses={201: CommentSerializer()},
        tags=['Comments']
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):
        logger.info(f"Creating a new comment by user {self.request.user.username}")
        serializer.save(author=self.request.user)
        logger.info("Comment successfully created")



