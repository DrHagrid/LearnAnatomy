# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-20 10:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0005_auto_20180619_1720'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoneType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('variable', models.CharField(max_length=32, verbose_name='Переменная')),
            ],
            options={
                'verbose_name': 'Тип кости',
                'verbose_name_plural': 'Типы костей',
            },
        ),
        migrations.AddField(
            model_name='bone',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='content.BoneType', verbose_name='Отдел скелета'),
        ),
    ]