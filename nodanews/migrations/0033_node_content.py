# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-08 01:35
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0032_auto_20171006_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='content',
            field=tinymce.models.HTMLField(default='stuff here'),
        ),
    ]
