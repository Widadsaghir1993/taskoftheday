# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sb_mail', '0023_auto_20171003_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sb_mail_server',
            name='priority',
            field=models.BooleanField(default=False),
        ),
    ]
