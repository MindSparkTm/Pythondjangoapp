# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-26 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plentyofcats', '0015_auto_20180624_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Europeads',
            fields=[
                ('postid', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=10000, null=True)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('uploaded_file', models.FileField(blank=True, null=True, upload_to='media/users/')),
                ('uploaded_file_url', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usads',
            fields=[
                ('postid', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(blank=True, max_length=10000, null=True)),
                ('description', models.CharField(blank=True, max_length=10000, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
                ('state', models.CharField(blank=True, max_length=30, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('uploaded_file', models.FileField(blank=True, null=True, upload_to='media/users/')),
                ('uploaded_file_url', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
