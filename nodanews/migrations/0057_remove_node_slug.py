# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-04-03 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0056_auto_20180403_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='slug',
        ),
    ]
