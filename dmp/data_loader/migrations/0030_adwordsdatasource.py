# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 15:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0029_auto_20170628_1210'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdwordsDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('conditions', models.CharField(max_length=255, verbose_name='Query condition list')),
                ('field_list', models.CharField(max_length=255, verbose_name='Field list to query')),
                ('date_range', models.CharField(max_length=255, verbose_name='Date range')),
                ('report_type', models.CharField(max_length=255, verbose_name='Report type')),
                ('oauth_key_file', models.FileField(default=None, upload_to='file_uploads', verbose_name='OAuth2 keyfile')),
            ],
            options={
                'verbose_name': 'Adwords Data source',
                'verbose_name_plural': 'Adwords Data sources',
            },
            bases=('data_loader.datasource',),
        ),
    ]
