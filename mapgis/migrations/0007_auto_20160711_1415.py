# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 14:15
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapgis', '0006_cameras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameras',
            name='geom',
            field=django.contrib.gis.db.models.fields.MultiPointField(srid=4326),
        ),
    ]
