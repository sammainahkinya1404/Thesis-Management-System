# Generated by Django 5.1.3 on 2025-01-15 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theses', '0002_thesis_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThesisProgress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milestone', models.CharField(max_length=255)),
                ('completed', models.BooleanField(default=False)),
                ('due_date', models.DateField()),
                ('thesis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='theses.thesis')),
            ],
        ),
    ]
