# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-16 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0070_politicalbiasnews_issue'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicalissue',
            name='description',
            field=models.TextField(default='description goes here'),
        ),
    ]
