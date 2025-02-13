# Generated by Django 5.1.3 on 2025-01-17 14:59

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theses', '0004_alter_thesis_teacher'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='teacher',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_theses', to=settings.AUTH_USER_MODEL),
        ),
    ]
