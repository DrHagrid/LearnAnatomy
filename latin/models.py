# -*- coding: utf-8 -*-
from django.db import models


class BoneType(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    variable = models.CharField(max_length=32, verbose_name='Переменная')
    picture = models.ImageField(upload_to='latin/bones/covers', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип кости'
        verbose_name_plural = 'Типы костей'


class Bone(models.Model):
    class_name = 'Кости'
    name_rus = models.CharField(max_length=64, verbose_name='Название на русском')
    name_lat = models.CharField(max_length=64, verbose_name='Название на латинском')
    type = models.ForeignKey(BoneType, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Отдел скелета')
    info = models.TextField(blank=True, null=True, verbose_name='Информация')
    picture = models.ImageField(upload_to='latin/bones', blank=True, null=True, verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Отображать данный элемент на сайте')

    def __str__(self):
        return "%s" % self.name_rus

    class Meta:
        verbose_name = 'Кость'
        verbose_name_plural = 'Кости'


class MuscleType(models.Model):
    name = models.CharField(max_length=32, verbose_name='Название')
    variable = models.CharField(max_length=32, verbose_name='Переменная')
    picture = models.ImageField(upload_to='latin/muscles/covers', blank=True, null=True, verbose_name='Изображение')

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тип мышцы'
        verbose_name_plural = 'Типы мышц'


class Muscle(models.Model):
    class_name = 'Мышцы'
    name_rus = models.CharField(max_length=64, verbose_name='Название на русском')
    name_lat = models.CharField(max_length=64, verbose_name='Название на латинском')
    type = models.ForeignKey(MuscleType, blank=True, null=True, on_delete=models.DO_NOTHING, verbose_name='Отдел')
    info = models.TextField(blank=True, null=True, verbose_name='Информация')
    picture = models.ImageField(upload_to='latin/muscles', blank=True, null=True, verbose_name='Изображение')
    is_active = models.BooleanField(default=True, verbose_name='Отображать данный элемент на сайте')

    def __str__(self):
        return "%s" % self.name_rus

    class Meta:
        verbose_name = 'Мышца'
        verbose_name_plural = 'Мышцы'


element_groups = {'bone': Bone, 'muscle': Muscle}
element_types = {'bone': BoneType, 'muscle': MuscleType}
