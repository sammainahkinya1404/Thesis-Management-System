# Generated by Django 5.1.3 on 2025-01-15 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='feedback',
            field=models.TextField(blank=True, null=True),
        ),
    ]
