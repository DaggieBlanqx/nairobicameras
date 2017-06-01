# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 15:15
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objectid_1', models.IntegerField()),
                ('county_nam', models.CharField(max_length=50)),
                ('shape_leng', models.FloatField()),
                ('shape_area', models.FloatField()),
                ('nema_regio', models.CharField(max_length=50)),
                ('eprc_regio', models.CharField(max_length=50)),
                ('eppc_addit', models.CharField(max_length=50)),
                ('highriskma', models.CharField(max_length=5)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=21037)),
            ],
        ),
    ]
