# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-02 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0046_auto_20180131_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=750)),
                ('url', models.CharField(default='', max_length=750)),
            ],
        ),
    ]
