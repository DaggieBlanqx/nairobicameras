# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-11 16:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mapgis', '0014_auto_20160711_1650'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accidents',
            old_name='name',
            new_name='time',
        ),
    ]
