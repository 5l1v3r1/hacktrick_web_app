# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0019_auto_20170308_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='training',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
