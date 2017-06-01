# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 13:54
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapgis', '0005_rails'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cameras',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=21037)),
            ],
        ),
    ]
