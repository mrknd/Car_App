# Generated by Django 5.0.6 on 2024-05-29 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_remove_car_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='doors',
            field=models.IntegerField(),
        ),
    ]
