# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='name',
        ),
    ]
