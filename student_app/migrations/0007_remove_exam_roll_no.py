# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 11:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0006_remove_class_no_of_classes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='roll_no',
        ),
    ]
