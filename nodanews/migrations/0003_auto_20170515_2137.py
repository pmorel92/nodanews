# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-16 04:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0002_auto_20170515_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='node_dir',
            options={'ordering': ('-date_updated', 'name')},
        ),
    ]
