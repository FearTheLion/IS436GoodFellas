# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0002_auto_20190425_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='major',
            name='related_major',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='launchscreen.Major'),
        ),
    ]
