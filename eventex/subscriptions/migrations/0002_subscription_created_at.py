# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-18 15:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 2, 18, 15, 4, 25, 839276, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
