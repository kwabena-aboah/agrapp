# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-07 18:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=250)),
                ('address2', models.CharField(blank=True, max_length=250, null=True)),
                ('zip_or_postal_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('fax_number', models.CharField(blank=True, max_length=20, null=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('allow_billing', models.BooleanField(default=True, help_text='Allow billing from this country')),
                ('allow_shipping', models.BooleanField(default=True, help_text='Allow shipping to this country')),
                ('iso_code2', models.CharField(help_text='Two letter ISO code', max_length=2, unique=True)),
                ('iso_code3', models.CharField(help_text='Three letter ISO code', max_length=3, unique=True)),
                ('iso_numeric', models.IntegerField(help_text='Numeric ISO code')),
                ('subject_to_vat', models.BooleanField(default=False, help_text='Is VAT applicable')),
                ('display_order', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('display_order', 'name'),
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('code', models.CharField(help_text='Abbrevation', max_length=10)),
                ('is_active', models.BooleanField(default=True)),
                ('display_order', models.IntegerField(default=0)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('updated_by', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Country')),
            ],
            options={
                'ordering': ('display_order', 'name'),
            },
        ),
        migrations.AddField(
            model_name='address',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Country', verbose_name='your text'),
        ),
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='address',
            name='state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.State'),
        ),
    ]
