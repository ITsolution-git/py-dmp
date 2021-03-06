# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 22:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0024_dynamodbdatasource_httpdatasource_twitterdatasource_zendeskdatasource'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmazonS3DataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('bucket', models.CharField(max_length=255, verbose_name='S3 bucket name')),
                ('path_prefix', models.CharField(max_length=255, verbose_name='Path prefix')),
                ('access_key', models.CharField(max_length=255, verbose_name='Access key')),
                ('secret_key', models.CharField(max_length=255, verbose_name='Secret key')),
                ('endpoint', models.CharField(max_length=255, verbose_name='Endpoint URL')),
            ],
            options={
                'verbose_name_plural': 'AmazonS3 Data sources',
                'verbose_name': 'AmazonS3 Data source',
            },
            bases=('data_loader.datasource',),
        ),
        migrations.CreateModel(
            name='MySQLDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('host', models.CharField(max_length=255, verbose_name='Host')),
                ('port', models.CharField(max_length=255, verbose_name='Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('database', models.CharField(max_length=255, verbose_name='Database')),
            ],
            options={
                'verbose_name_plural': 'MySQL Data sources',
                'verbose_name': 'MySQL Data source',
            },
            bases=('data_loader.datasource',),
        ),
        migrations.CreateModel(
            name='RedshiftDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('host', models.CharField(max_length=255, verbose_name='Host')),
                ('port', models.CharField(max_length=255, verbose_name='Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('database', models.CharField(max_length=255, verbose_name='Database')),
                ('schema_name', models.CharField(max_length=255, verbose_name='Destination schema name')),
            ],
            options={
                'verbose_name_plural': 'Redshift Data sources',
                'verbose_name': 'Redshift Data source',
            },
            bases=('data_loader.datasource',),
        ),
    ]
