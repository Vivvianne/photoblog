# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-07-20 09:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]