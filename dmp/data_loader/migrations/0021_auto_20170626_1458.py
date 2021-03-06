# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-26 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_loader', '0020_auto_20170626_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='FTPDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('host', models.CharField(max_length=255, verbose_name='Host')),
                ('port', models.CharField(max_length=255, verbose_name='Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('prefix', models.CharField(max_length=255, verbose_name='Database')),
            ],
            options={
                'verbose_name_plural': 'FTP Data sources',
                'verbose_name': 'FTP Data source',
            },
            bases=('data_loader.datasource',),
        ),
        migrations.CreateModel(
            name='JDBCDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('url', models.CharField(max_length=255, verbose_name='Host')),
                ('driver_class', models.CharField(max_length=255, verbose_name='Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
            ],
            options={
                'verbose_name_plural': 'JDBC Data sources',
                'verbose_name': 'JDBC Data source',
            },
            bases=('data_loader.datasource',),
        ),
        migrations.CreateModel(
            name='MongoDBDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('uri', models.CharField(max_length=255, verbose_name='URI')),
                ('hosts', models.CharField(max_length=255, verbose_name='Hosts')),
                ('port', models.CharField(max_length=255, verbose_name='Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('database', models.CharField(max_length=255, verbose_name='Database')),
            ],
            options={
                'verbose_name_plural': 'MongoDB Data sources',
                'verbose_name': 'MongoDB Data source',
            },
            bases=('data_loader.datasource',),
        ),
        migrations.CreateModel(
            name='OracleDBDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('host', models.CharField(max_length=255, verbose_name='Host')),
                ('port', models.CharField(max_length=255, verbose_name='Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('database', models.CharField(max_length=255, verbose_name='Database')),
                ('schema_name', models.CharField(max_length=255, verbose_name='Schema name')),
            ],
            options={
                'verbose_name_plural': 'OracleDB Data sources',
                'verbose_name': 'OracleDB Data source',
            },
            bases=('data_loader.datasource',),
        ),
        migrations.CreateModel(
            name='VerticaDataSource',
            fields=[
                ('data_source', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='data_loader.DataSource')),
                ('host', models.CharField(max_length=255, verbose_name='Host')),
                ('port', models.CharField(max_length=255, verbose_name='Port')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('database', models.CharField(max_length=255, verbose_name='Database')),
                ('schema_name', models.FileField(max_length=255, upload_to='', verbose_name='Schema name')),
            ],
            options={
                'verbose_name_plural': 'Vertica Data sources',
                'verbose_name': 'Vertica Data source',
            },
            bases=('data_loader.datasource',),
        ),
        migrations.AlterField(
            model_name='postgresqldatasource',
            name='schema_file',
            field=models.FileField(default=None, upload_to='file_uploads', verbose_name='Schema file'),
        ),
    ]
