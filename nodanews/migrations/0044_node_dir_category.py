# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-12-15 01:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0043_auto_20171214_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='node_dir',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='nodanews.Breaking_Category'),
        ),
    ]