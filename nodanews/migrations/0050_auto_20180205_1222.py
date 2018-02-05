# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-05 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0049_politicalbiasnews'),
    ]

    operations = [
        migrations.AddField(
            model_name='breaking_link',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='media/nodes'),
        ),
        migrations.AddField(
            model_name='breaking_link',
            name='imageQ',
            field=models.BooleanField(default=False),
        ),
    ]