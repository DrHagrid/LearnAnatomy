# -*- coding: utf-8 -*-
from django.db import models


class SampleType(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    variable = models.CharField(max_length=32, verbose_name='Переменная')
    picture = models.ImageField(upload_to='histology/covers', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Sample(models.Model):
    correct_option = models.CharField(max_length=64, verbose_name='Верный вариант')
    type = models.ForeignKey(SampleType, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Раздел')
    options = models.TextField(default='', verbose_name='Все варианты', help_text='Впишите в это поле все варианты, включая верный, разделяя знаком ";"')
    info = models.TextField(blank=True, null=True, verbose_name='Информация о препарате', help_text='В данном поле вы можете использовать теги HTML')
    picture = models.ImageField(upload_to='histology/samples', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return "%s" % self.correct_option

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'
