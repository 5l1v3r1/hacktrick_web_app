# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-06 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hacktrick', '0048_auto_20180306_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertraining',
            name='user_status',
            field=models.BooleanField(default=False, verbose_name='Katılımcı durumu'),
        ),
    ]
