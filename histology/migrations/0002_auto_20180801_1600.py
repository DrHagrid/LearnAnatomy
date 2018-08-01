# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-01 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('histology', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sample',
            name='incorrect_options',
        ),
        migrations.AddField(
            model_name='sample',
            name='options',
            field=models.TextField(default='', help_text='Впишите в это поле все варианты, включая верный, разделяя знаком ";"', verbose_name='Все варианты'),
        ),
    ]