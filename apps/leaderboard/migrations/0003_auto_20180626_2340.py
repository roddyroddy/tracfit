# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-26 23:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard', '0002_auto_20180626_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='amrap_score',
            field=models.IntegerField(),
        ),
    ]
