# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-01 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correct_option', models.CharField(max_length=64, verbose_name='Верный вариант')),
                ('incorrect_options', models.TextField(help_text='Впишите в это поле варианты разделяя знаком ";"', verbose_name='Неверный варианты')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Информация о препарате')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='histology/samples', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Препарат',
                'verbose_name_plural': 'Препараты',
            },
        ),
    ]
