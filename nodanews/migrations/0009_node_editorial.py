# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-02 01:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0008_auto_20170518_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='editorial',
            field=models.BooleanField(default=False),
        ),
    ]
