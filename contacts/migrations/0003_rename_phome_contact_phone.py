# Generated by Django 5.0.6 on 2024-06-01 13:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_rename_contacts_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='phome',
            new_name='phone',
        ),
    ]
