# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-09 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0014_profile_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='connected',
            field=models.BooleanField(default=True),
        ),
    ]
