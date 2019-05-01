# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-25 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchscreen', '0005_major_avg_starting_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='major',
            name='major_major_interest_tag',
        ),
        migrations.RemoveField(
            model_name='major',
            name='major_minor_interest_tag',
        ),
        migrations.RemoveField(
            model_name='uni_class',
            name='class_major_interest_tag',
        ),
        migrations.RemoveField(
            model_name='uni_class',
            name='class_minor_interest_tag',
        ),
        migrations.AddField(
            model_name='major',
            name='interest_1',
            field=models.CharField(choices=[('Technology', 'tech'), ('Healthcare', 'health'), ('Artistic Expression', 'art'), ('Mathematics', 'math'), ('Science', 'science')], default='art', max_length=20),
        ),
        migrations.AddField(
            model_name='major',
            name='interest_2',
            field=models.CharField(choices=[('Exercise', 'exercise'), ('Travel', 'travel'), ('Hands-on', 'manual'), ('Critical Thinking', 'crit_think')], default='manual', max_length=20),
        ),
        migrations.AddField(
            model_name='uni_class',
            name='avg_starting_salary',
            field=models.CharField(choices=[('30,000 - 50,000', 'low'), ('50,000 - 80,000', 'med'), ('80,000+', 'high')], default='med', max_length=20),
        ),
        migrations.AddField(
            model_name='uni_class',
            name='interest_1',
            field=models.CharField(choices=[('Technology', 'tech'), ('Healthcare', 'health'), ('Artistic Expression', 'art'), ('Mathematics', 'math'), ('Science', 'science')], default='art', max_length=20),
        ),
        migrations.AddField(
            model_name='uni_class',
            name='interest_2',
            field=models.CharField(choices=[('Exercise', 'exercise'), ('Travel', 'travel'), ('Hands-on', 'manual'), ('Critical Thinking', 'crit_think')], default='manual', max_length=20),
        ),
    ]