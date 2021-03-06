# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('asset', '0004_auto_20160713_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='winconf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('repo', models.CharField(max_length=128)),
                ('localpath', models.CharField(max_length=64)),
                ('env', models.IntegerField(blank=True, choices=[(1, '\u751f\u4ea7\u73af\u5883'), (2, '\u6d4b\u8bd5\u73af\u5883')], null=True, verbose_name='\u8fd0\u884c\u73af\u5883')),
                ('servicename', models.CharField(max_length=32)),
                ('tasklist_name', models.CharField(max_length=32, unique=True)),
                ('hostname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.minion')),
            ],
        ),
    ]
