
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='level',
        ),
        migrations.RemoveField(
            model_name='trainingplan',
            name='level',
        ),
        migrations.RemoveField(
            model_name='schedule',
            name='training_plan',
        ),
        migrations.RemoveField(
            model_name='trainingplan',
            name='exercises',
        ),
        migrations.RemoveField(
            model_name='trainingplanexercise',
            name='training_plan',
        ),
        migrations.RemoveField(
            model_name='trainingplanexercise',
            name='exercise',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='calories_burned_per_minute',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='intensity',
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='muscle_groups',
        ),
        migrations.RemoveField(
            model_name='exercisecategory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='exercisecategory',
            name='parent_category',
        ),
        migrations.RemoveField(
            model_name='exercisecategory',
            name='popularity_score',
        ),
        migrations.AddField(
            model_name='exercise',
            name='execution',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='exercise',
            name='starting_position',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='exercisecategory',
            name='image',
            field=models.ImageField(default='images/default1.svg', upload_to='images/'),
        ),
        migrations.RemoveField(
            model_name='exercise',
            name='equipment_needed',
        ),
        migrations.DeleteModel(
            name='ExerciseLevel',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='TrainingPlan',
        ),
        migrations.DeleteModel(
            name='TrainingPlanExercise',
        ),
        migrations.AddField(
            model_name='exercise',
            name='equipment_needed',
            field=models.ManyToManyField(blank=True, related_name='exercises', to='exercise_management.equipmentcategory'),
        ),
    ]
