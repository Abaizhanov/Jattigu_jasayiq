import logging
from django.shortcuts import render
from user.permissions import IsAdminUser, IsRegularUser
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import User
from .serializer import MyTokenObtainPairSerializer, RegisterSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Initialize logger
logger = logging.getLogger('user')

# JWT Token View
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    @swagger_auto_schema(
        operation_description="Obtain a JWT token by providing valid credentials.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password'),
            },
            required=['username', 'password'],
        ),
        responses={
            200: "Token generated successfully",
            401: "Invalid credentials",
        },
    )
    def post(self, request, *args, **kwargs):
        username = request.data.get('username') or request.data.get('email', 'Unknown')
        logger.info("Token requested by user: %s", username)
        response = super().post(request, *args, **kwargs)
        logger.info("Token successfully generated for user: %s", username)
        return response


# User Registration View
class RegisterView(generics.CreateAPIView):
    """
    Endpoint for user registration.
    """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    @swagger_auto_schema(
        operation_description="Register a new user.",
        request_body=RegisterSerializer,
        responses={
            201: "User registered successfully",
            400: "Validation error",
        },
    )
    def perform_create(self, serializer):
        logger.info(f"New user registration attempt: {serializer.validated_data.get('email')}")
        super().perform_create(serializer)
        logger.info(f"User registered successfully: {serializer.validated_data.get('email')}")


# Get All Available Routes
@swagger_auto_schema(
    method='get',
    operation_description="Fetch all available API routes.",
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'path': openapi.Schema(type=openapi.TYPE_STRING, description='API path'),
                    'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the API'),
                },
            ),
        ),
    },
)
@api_view(['GET'])
def getRoutes(request):
    """
    Returns all available API routes.
    """
    logger.info("Fetching available API routes")
    routes = [
        {'path': '/api/token/', 'description': 'Obtain JWT token'},
        {'path': '/api/register/', 'description': 'Register a new user'},
        {'path': '/api/token/refresh/', 'description': 'Refresh JWT token'},
        {'path': '/api/test/', 'description': 'Test endpoint with GET and POST (requires authentication)'},
    ]
    return Response(routes, status=status.HTTP_200_OK)


# Test Endpoint
@swagger_auto_schema(
    method='get',
    operation_description="Test endpoint with GET request.",
    responses={
        200: "Successfully handled GET request.",
    },
)
@swagger_auto_schema(
    method='post',
    operation_description="Test endpoint with POST request. Provide 'text' in request body.",
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'text': openapi.Schema(type=openapi.TYPE_STRING, description='Text to include in the response'),
        },
    ),
    responses={
        200: "Successfully handled POST request.",
        400: "Bad request format.",
    },
)
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def testEndPoint(request):
    """
    Example endpoint to test API responses.
    """
    logger.info("Test endpoint accessed by user: %s", request.user.username)

    if request.method == 'GET':
        data = f"Congratulations {request.user}, your API just responded to a GET request."
        logger.info("Responding to GET request")
        return Response({'response': data}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        text = request.data.get('text', 'Hello buddy')
        data = f"Congratulations! Your API just responded to a POST request with text: {text}"
        logger.info("Responding to POST request with text: %s", text)
        return Response({'response': data}, status=status.HTTP_200_OK)
    
    logger.error("Invalid request method accessed by user: %s", request.user.username)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_400_BAD_REQUEST)


class AdminOnlyView(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_description="Access admin-only view.",
        responses={200: "Welcome, Admin!"},
    )
    def get(self, request):
        logger.info("Admin-only view accessed by admin user: %s", request.user.username)
        return Response({"message": "Hello, Admin!"})
    

class UserOnlyView(APIView):
    permission_classes = [IsRegularUser]

    @swagger_auto_schema(
        operation_description="Access user-only view.",
        responses={200: "Welcome, User!"},
    )
    def get(self, request):
        logger.info("User-only view accessed by user: %s", request.user.username)
        return Response({"message": "Hello, User!"})

