# Generated by Django 4.2.5 on 2024-07-27 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': [('special_status', 'Can read all found books')]},
        ),
    ]
