# -*- coding: utf-8 -*-
from django.db import models


class Sample(models.Model):
    correct_option = models.CharField(max_length=64, verbose_name='Верный вариант')
    options = models.TextField(default='', verbose_name='Все варианты', help_text='Впишите в это поле все варианты, включая верный, разделяя знаком ";"')
    info = models.TextField(blank=True, null=True, verbose_name='Информация о препарате')
    picture = models.ImageField(upload_to='histology/samples', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return "%s" % self.correct_option

    class Meta:
        verbose_name = 'Препарат'
        verbose_name_plural = 'Препараты'
