# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 09:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0036_auto_20170313_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='speaker',
            name='is_visible',
            field=models.BooleanField(default=True, verbose_name='Görülebilir'),
        ),
    ]
