
# Generated by Django 5.1.2 on 2024-12-02 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise_management', '0003_alter_exercise_equipment_needed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercisecategory',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/'),
        ),
    ]

