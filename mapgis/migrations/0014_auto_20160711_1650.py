# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapgis', '0013_auto_20160711_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accidents',
            old_name='constituen',
            new_name='description',
        ),
    ]