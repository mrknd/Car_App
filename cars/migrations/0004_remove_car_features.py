# Generated by Django 5.0.6 on 2024-05-29 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_description_alter_car_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='features',
        ),
    ]
