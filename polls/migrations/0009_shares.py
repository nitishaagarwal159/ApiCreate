# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shares',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postshared', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Posts')),
                ('postsharedby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.employees')),
            ],
        ),
    ]
