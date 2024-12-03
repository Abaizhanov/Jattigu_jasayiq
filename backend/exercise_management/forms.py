
# forms.py
from django import forms
from .models import Exercise, ExerciseCategory, EquipmentCategory

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'starting_position', 'execution', 'category', 'equipment_needed']
        widgets = {
            'category': forms.CheckboxSelectMultiple(),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'starting_position': forms.Textarea(attrs={'class': 'form-control'}),
            'execution': forms.Textarea(attrs={'class': 'form-control'}),
            'equipment_needed': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
        }

class ExerciseCategoryForm(forms.ModelForm):
    class Meta:
        model = ExerciseCategory
        fields = ['name', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class EquipmentCategoryForm(forms.ModelForm):
    class Meta:
        model = EquipmentCategory
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }