# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-19 18:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0013_node_related'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='node',
            name='related',
        ),
    ]
