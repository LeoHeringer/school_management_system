# Generated by Django 5.1 on 2024-08-12 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classes', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_created', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='classes.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='students.student')),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
                'ordering': ['student', 'class_name', 'subject'],
            },
        ),
    ]
