# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-16 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0016_auto_20170726_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='bg_image',
        ),
        migrations.RemoveField(
            model_name='node_dir',
            name='related',
        ),
        migrations.AddField(
            model_name='node_dir',
            name='banner',
            field=models.ImageField(blank=True, default='', upload_to='media/nodes'),
        ),
        migrations.AddField(
            model_name='node_dir',
            name='description',
            field=models.TextField(default=' '),
        ),
    ]
