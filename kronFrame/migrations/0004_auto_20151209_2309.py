# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kronFrame', '0003_auto_20151209_1235'),
    ]

    operations = [
        migrations.AddField(
            model_name='offered',
            name='class_day',
            field=models.CharField(choices=[('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday')], default='Mon', max_length=3),
        ),
        migrations.AlterField(
            model_name='offered',
            name='end_time',
            field=models.CharField(choices=[(3, '09:00'), (4, '09:30'), (5, '10:00'), (6, '10:30'), (7, '11:00'), (8, '11:30'), (9, '12:00'), (10, '12:30'), (11, '01:00'), (12, '01:30'), (13, '02:00'), (14, '02:30'), (15, '03:00'), (16, '03:30'), (17, '04:00'), (18, '05:00'), (19, '05:30')], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='offered',
            name='start_time',
            field=models.CharField(choices=[(1, '08:00'), (2, '08:30'), (3, '09:00'), (4, '09:30'), (5, '10:00'), (6, '10:30'), (7, '11:00'), (8, '11:30'), (9, '12:00'), (10, '12:30'), (11, '01:00'), (12, '01:30'), (13, '02:00'), (14, '02:30'), (15, '03:00'), (16, '03:30'), (17, '04:00')], default=1, max_length=2),
        ),
    ]
