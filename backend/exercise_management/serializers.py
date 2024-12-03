from rest_framework import serializers
from .models import Exercise, ExerciseCategory, EquipmentCategory
from rest_framework.exceptions import ValidationError


class ExerciseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseCategory
        fields = ['id', 'name', 'image']


class EquipmentCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentCategory
        fields = ['id', 'name']


class ExerciseSerializer(serializers.ModelSerializer):
    category = ExerciseCategorySerializer(many=True)  # Nested serializer for categories
    equipment_needed = EquipmentCategorySerializer(many=True)  # Nested serializer for equipment

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'starting_position', 'execution', 'category', 'equipment_needed',
                  'image']


