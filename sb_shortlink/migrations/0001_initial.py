# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 07:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('analytics', '0046_auto_20171011_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='shortlink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short', models.URLField(blank=True, null=True, verbose_name='Shorten URL')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('expire_date', models.DateTimeField(blank=True, null=True, verbose_name='Expire Time')),
                ('active', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                             to=settings.AUTH_USER_MODEL, verbose_name='Active')),
                ('user_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                              to='analytics.Profile', verbose_name='User Id')),
            ],
        ),
    ]
