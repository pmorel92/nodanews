# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-06-18 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0080_auto_20190618_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='stf',
            name='video',
            field=models.CharField(blank=True, default=b'', max_length=500),
        ),
        migrations.AddField(
            model_name='stf',
            name='videoQ',
            field=models.BooleanField(default=False),
        ),
    ]
