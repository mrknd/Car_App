# Generated by Django 5.0.6 on 2024-05-29 12:48

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_remove_car_features'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(default='Standard Features'),
            preserve_default=False,
        ),
    ]
