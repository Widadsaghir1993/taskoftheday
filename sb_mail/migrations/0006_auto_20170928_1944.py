# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('sb_mail', '0005_email_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sbmail_template',
            name='object',
            field=models.CharField(max_length=90),
        ),
    ]
