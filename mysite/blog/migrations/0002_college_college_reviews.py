# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-03 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='college_reviews',
            field=models.TextField(null=True),
        ),
    ]
