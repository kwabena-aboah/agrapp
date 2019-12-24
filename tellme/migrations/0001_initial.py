# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-24 22:06
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
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255, verbose_name='Url')),
                ('browser', models.TextField(verbose_name='Browser')),
                ('comment', models.TextField(verbose_name='Comment')),
                ('screenshot', models.ImageField(blank=True, null=True, upload_to=b'tellme/screenshots/', verbose_name='Screenshot')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Creation date')),
                ('ack', models.BooleanField(default=False, verbose_name='Acknowledgement')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'feedback',
                'verbose_name_plural': 'feedbacks',
            },
        ),
    ]