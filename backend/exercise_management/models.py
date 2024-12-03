
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    starting_position = models.TextField(default='')
    execution = models.TextField(default='')

    category = models.ManyToManyField('ExerciseCategory', related_name='exercises')
    equipment_needed = models.ManyToManyField('EquipmentCategory', related_name='exercises')
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name

class ExerciseCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', default='images/default.jpg')

    def __str__(self):
        return self.name

class EquipmentCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

