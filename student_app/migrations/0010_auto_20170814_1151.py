# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0009_auto_20170814_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='total_marks',
            new_name='total_marks_in_class',
        ),
    ]
