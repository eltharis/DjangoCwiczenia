# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seresults', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchrequest',
            old_name='seaech_engine',
            new_name='search_engine',
        ),
    ]