# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sb_mail', '0029_auto_20171004_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='sb_settings',
            name='rank',
            field=models.IntegerField(default=1),
        ),
    ]