import logging
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.shortcuts import get_object_or_404
from .models import Exercise, ExerciseCategory, EquipmentCategory
from .serializers import ExerciseSerializer, ExerciseCategorySerializer, EquipmentCategorySerializer

logger = logging.getLogger('exercise')

# List all exercises
class ExerciseListView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    @swagger_auto_schema(operation_description="Retrieve a list of all exercises.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new exercise.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


@swagger_auto_schema(
    method='post',
    request_body=ExerciseSerializer,
    responses={201: ExerciseSerializer, 400: "Bad Request"},
    operation_description="Create a new exercise.",
)
@api_view(['POST'])
def exercise_create(request):
    serializer = ExerciseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Exercise created: {serializer.data}")
        return Response(serializer.data, status=201)
    logger.error(f"Exercise creation failed: {serializer.errors}")
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='put',
    request_body=ExerciseSerializer,
    responses={200: ExerciseSerializer, 400: "Bad Request"},
    operation_description="Update an existing exercise.",
)
@api_view(['PUT'])
def exercise_update(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    serializer = ExerciseSerializer(exercise, data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Exercise updated: {serializer.data}")
        return Response(serializer.data)
    logger.error(f"Exercise update failed for pk={pk}: {serializer.errors}")
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='delete',
    responses={204: "No Content"},
    operation_description="Delete an exercise.",
)
@api_view(['DELETE'])
def exercise_delete(request, pk):
    exercise = get_object_or_404(Exercise, pk=pk)
    exercise.delete()
    logger.info(f"Exercise deleted: pk={pk}")
    return Response(status=204)


class ExerciseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    @swagger_auto_schema(operation_description="Retrieve details of a specific exercise.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific exercise.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific exercise.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Exercise Category Views
class ExerciseCategoryListView(generics.ListCreateAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

    @swagger_auto_schema(operation_description="Retrieve a list of all exercise categories.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new exercise category.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
@swagger_auto_schema(
    method='post',
    request_body=ExerciseCategorySerializer,
    responses={201: ExerciseCategorySerializer, 400: "Bad Request"},
    operation_description="Create a new exercise category.",
)
@api_view(['POST'])
def exercise_category_create(request):
    """
    Create a new exercise category.
    """
    serializer = ExerciseCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Exercise category created: {serializer.data}")
        return Response(serializer.data, status=201)
    logger.error(f"Exercise category creation failed: {serializer.errors}")
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='put',
    request_body=ExerciseCategorySerializer,
    responses={200: ExerciseCategorySerializer, 400: "Bad Request"},
    operation_description="Update an existing exercise category.",
)
@api_view(['PUT'])
def exercise_category_update(request, pk):
    category = get_object_or_404(ExerciseCategory, pk=pk)
    serializer = ExerciseCategorySerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Exercise category updated: {serializer.data}")
        return Response(serializer.data)
    logger.error(f"Exercise category update failed for pk={pk}: {serializer.errors}")
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='delete',
    responses={204: "No Content"},
    operation_description="Delete an exercise category.",
)
@api_view(['DELETE'])
def exercise_category_delete(request, pk):
    category = get_object_or_404(ExerciseCategory, pk=pk)
    category.delete()
    logger.info(f"Exercise category deleted: pk={pk}")
    return Response(status=204)


class ExerciseCategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExerciseCategory.objects.all()
    serializer_class = ExerciseCategorySerializer

    @swagger_auto_schema(operation_description="Retrieve details of a specific exercise category.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific exercise category.")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific exercise category.")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# Equipment Category Views
class EquipmentCategoryListView(generics.ListCreateAPIView):
    queryset = EquipmentCategory.objects.all()
    serializer_class = EquipmentCategorySerializer

    @swagger_auto_schema(operation_description="Retrieve a list of all equipment categories.")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new equipment category.")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
@swagger_auto_schema(
    method='post',
    request_body=EquipmentCategorySerializer,
    responses={201: EquipmentCategorySerializer, 400: "Bad Request"},
    operation_description="Create a new equipment category.",
)
@api_view(['POST'])
def equipment_category_create(request):
    """
    Create a new equipment category.
    """
    serializer = EquipmentCategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        logger.info(f"Equipment category created: {serializer.data}")
        return Response(serializer.data, status=201)
    logger.error(f"Equipment category creation failed: {serializer.errors}")
    return Response(serializer.errors, status=400)


@swagger_auto_schema(
    method='delete',
    responses={204: "No Content"},
    operation_description="Delete an equipment category.",
)
@api_view(['DELETE'])
def equipment_category_delete(request, pk):
    category = get_object_or_404(EquipmentCategory, pk=pk)
    category.delete()
    logger.info(f"Equipment category deleted: pk={pk}")
    return Response(status=204)



