
# exercise_management/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('exercises/', views.ExerciseListView.as_view(), name='exercise_list'),
    path('exercises/<int:pk>/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise_categories/', views.ExerciseCategoryListView.as_view(), name='exercise_category_list'),
    path('exercise_categories/<int:pk>/', views.ExerciseCategoryDetailView.as_view(), name='exercise_category_detail'),
    path('exercise_categories/create/', views.exercise_category_create, name='exercise_category_create'),
    path('exercise_categories/<int:pk>/update/', views.exercise_category_update, name='exercise_category_update'),
    path('exercise_categories/<int:pk>/delete/', views.exercise_category_delete, name='exercise_category_delete'),
    path('equipment_categories/', views.EquipmentCategoryListView.as_view(), name='equipment_category_list'),
    path('equipment_category/create/', views.equipment_category_create, name='equipment_category_create'),
    path('exercise/update/<int:pk>/', views.exercise_update, name='exercise_update'),
]


