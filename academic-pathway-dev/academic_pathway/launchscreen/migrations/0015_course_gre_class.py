# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-30 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0014_auto_20190430_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='gre_class',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
