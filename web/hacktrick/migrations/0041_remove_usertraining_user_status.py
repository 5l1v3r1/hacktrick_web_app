# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-02-18 13:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0040_auto_20180218_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usertraining',
            name='user_status',
        ),
    ]