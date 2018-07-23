# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-07 18:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(help_text='ISO Currency Code', max_length=3, unique=True)),
                ('exchange_rate', models.FloatField(default=1.0)),
                ('locale', models.CharField(blank=True, max_length=10)),
                ('display_format', models.CharField(help_text='Display format: 1.2 => "${0:,.2f}".format(price) => $1.20 (python format string)', max_length=50)),
                ('is_primary', models.BooleanField(default=False, help_text='Default currency of prices & costs. When you change primary currency, make sure to update exchange rates, prices & costs.')),
                ('is_active', models.BooleanField(default=False)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('id',),
                'verbose_name_plural': 'Currencies',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('method', models.CharField(choices=[('PE', 'Percentage'), ('FI', 'Fixed')], help_text='Tax deduction method: fixed tax per product or percentage (in fraction) of price per product', max_length=2)),
                ('rate', models.FloatField(default=0.0)),
                ('updated_by', models.CharField(max_length=100)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'financial_tax',
                'verbose_name_plural': 'Taxes',
            },
        ),
    ]