# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-15 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('contact', models.CharField(default='', max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, default='', max_length=300)),
                ('title', models.CharField(blank=True, default='', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Media_Org',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('date_posted', models.DateTimeField()),
                ('home_page', models.CharField(default='', max_length=200)),
                ('country', models.CharField(default='', max_length=100)),
                ('date_founded', models.DateField(default='1956-02-27')),
                ('logo', models.ImageField(upload_to='media/logos')),
                ('description', models.TextField()),
                ('fake_or_not', models.BooleanField(default=False)),
                ('ready', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(default='', max_length=200)),
                ('country', models.CharField(default='', max_length=100)),
                ('date_posted', models.DateTimeField()),
                ('my_take', models.TextField()),
                ('head_image', models.ImageField(default='', upload_to='media/nodes')),
                ('foot_image', models.ImageField(default='', upload_to='media/nodes')),
                ('bg_image', models.ImageField(blank=True, default='', upload_to='media/nodes')),
                ('video_embed1', models.CharField(blank=True, default='', max_length=500)),
                ('video_embed2', models.CharField(blank=True, default='', max_length=500)),
                ('video_embed3', models.CharField(blank=True, default='', max_length=500)),
                ('hotness', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ('-date_posted',),
            },
        ),
        migrations.CreateModel(
            name='Node_Dir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('date_updated', models.DateTimeField(default='1949-08-08')),
                ('related', models.ManyToManyField(blank=True, related_name='_node_dir_related_+', to='nodanews.Node_Dir')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Perspective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=47)),
                ('node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodanews.Node')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('color', models.CharField(default='', max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='node',
            name='node_direc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodanews.Node_Dir'),
        ),
        migrations.AddField(
            model_name='node',
            name='region',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='nodanews.Region'),
        ),
        migrations.AddField(
            model_name='link',
            name='media',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodanews.Media_Org'),
        ),
        migrations.AddField(
            model_name='link',
            name='perspective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodanews.Perspective'),
        ),
        migrations.AddField(
            model_name='journalist',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nodanews.Media_Org'),
        ),
    ]
