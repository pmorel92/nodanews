# Generated by Django 2.1.1 on 2018-09-18 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nodanews', '0077_node_dir_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='node_dir',
            name='slug',
            field=models.SlugField(default=' ', max_length=100),
        ),
    ]