# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-06 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0059_headline_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='livevideo',
            name='name4',
            field=models.CharField(default='name goes here', max_length=200),
        ),
        migrations.AddField(
            model_name='livevideo',
            name='video4',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]