# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0011_auto_20170307_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='ticket_status',
            field=models.BooleanField(default=True),
        ),
    ]
