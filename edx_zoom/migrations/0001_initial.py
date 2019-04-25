# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-12 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import opaque_keys.edx.django.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LTICredential',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', opaque_keys.edx.django.models.CourseKeyField(max_length=255, unique=True)),
                ('key', models.CharField(max_length=255)),
                ('secret', models.CharField(max_length=255)),
            ],
        ),
    ]