# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-07-20 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_image_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_path',
            field=models.ImageField(upload_to='images/'),
        ),
    ]