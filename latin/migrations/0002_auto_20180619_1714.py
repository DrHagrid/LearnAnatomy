# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-19 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('latin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bone',
            name='info',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Информация'),
        ),
        migrations.AlterField(
            model_name='bone',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активность'),
        ),
        migrations.AlterField(
            model_name='bone',
            name='name_lat',
            field=models.CharField(max_length=64, verbose_name='Название на латинском'),
        ),
        migrations.AlterField(
            model_name='bone',
            name='name_rus',
            field=models.CharField(max_length=64, verbose_name='Название на русском'),
        ),
        migrations.AlterField(
            model_name='bone',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/media', verbose_name='Изображение'),
        ),
    ]
