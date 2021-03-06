# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 09:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=100)),
                ('no_of_classes', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_type', models.CharField(blank=True, max_length=150, null=True)),
                ('roll_no', models.CharField(blank=True, max_length=130, null=True)),
                ('exam_date', models.DateField(blank=True, null=True)),
                ('exam_roll_no', models.CharField(blank=True, max_length=130, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(blank=True, null=True)),
                ('exam', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='student_app.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=15, null=True)),
                ('last_name', models.CharField(blank=True, max_length=15, null=True)),
                ('roll_no', models.IntegerField(blank=True, null=True, unique=True)),
                ('mobile_no', models.CharField(blank=True, max_length=15, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=225, null=True)),
                ('student_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='student_app.Class')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(blank=True, max_length=150, null=True)),
                ('sub_code', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('student', models.ManyToManyField(to='student_app.Student')),
            ],
        ),
        migrations.AddField(
            model_name='mark',
            name='student_id',
            field=models.ManyToManyField(to='student_app.Student'),
        ),
        migrations.AddField(
            model_name='mark',
            name='subject_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='marks', to='student_app.Subject'),
        ),
        migrations.AddField(
            model_name='exam',
            name='student',
            field=models.ManyToManyField(to='student_app.Student'),
        ),
        migrations.AddField(
            model_name='exam',
            name='subject_id',
            field=models.ManyToManyField(to='student_app.Subject'),
        ),
    ]
