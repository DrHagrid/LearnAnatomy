# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-20 10:47
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
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('all', models.IntegerField(verbose_name='Общее количество выполненных заданий')),
                ('mistakes', models.IntegerField(verbose_name='Количество ошибок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Информация о пользователе',
                'verbose_name_plural': 'Информация о пользователях',
            },
        ),
    ]