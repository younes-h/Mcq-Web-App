# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 10:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0022_usertests'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserTests',
            new_name='UserTest',
        ),
    ]
