# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-25 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0012_auto_20170525_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datasource',
            name='account_id',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name='Account ID'),
        ),
        migrations.AlterField(
            model_name='datasource',
            name='upload_file',
            field=models.FileField(blank=True, default=None, null=True, upload_to='file_uploads', verbose_name='Upload file'),
        ),
    ]
