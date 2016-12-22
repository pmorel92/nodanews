# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-26 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0015_auto_20170726_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='media_org',
            name='media_character',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodanews.Media_Character'),
        ),
        migrations.AddField(
            model_name='media_org',
            name='political_lean',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodanews.Political_Lean'),
        ),
    ]
