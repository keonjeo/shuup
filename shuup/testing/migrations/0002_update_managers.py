# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-22 23:00
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('shuup_testing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='carrierwithcheckoutphase',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='paymentwithcheckoutphase',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterModelManagers(
            name='pseudopaymentprocessor',
            managers=[
                ('_default_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
