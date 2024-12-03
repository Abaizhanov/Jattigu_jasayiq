
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_management', '0004_alter_exercisecategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='category',
            field=models.ManyToManyField(related_name='exercises', to='exercise_management.ExerciseCategory'),
        ),
        migrations.AlterField(
            model_name='exercise',
            name='equipment_needed',
            field=models.ManyToManyField(related_name='exercises', to='exercise_management.EquipmentCategory'),
        ),
    ]
