
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_management', '0002_equipmentcategory_remove_exercise_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='equipment_needed',
            field=models.ManyToManyField(related_name='exercises', to='exercise_management.equipmentcategory'),
        ),
    ]
