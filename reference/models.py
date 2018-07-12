# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class ArticleSection(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    variable = models.CharField(max_length=32, verbose_name='Переменная')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'


class Article(models.Model):
    section = models.ForeignKey(ArticleSection, on_delete=models.DO_NOTHING, verbose_name='Раздел')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое', help_text='В данном поле вы можете использовать теги HTML')
    tags = models.CharField(max_length=256, verbose_name='Теги')
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s" % self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
