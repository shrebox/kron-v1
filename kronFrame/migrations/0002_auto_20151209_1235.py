# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-09 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kronFrame', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_credits',
            field=models.IntegerField(choices=[(2, 2), (4, 4)], default=4, max_length=1),
        ),
    ]
