# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-12 16:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0020_livevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalist',
            name='picture',
            field=models.ImageField(default=' ', upload_to='media/logos'),
        ),
    ]
