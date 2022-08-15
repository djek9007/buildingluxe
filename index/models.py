# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.urls import reverse
from django.utils import timezone



class About(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано')
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(blank=True, default='', verbose_name='Текст', )
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
    slug = models.SlugField(verbose_name='Url', blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'

    def __str__(self):
        return self.title

class Service(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано')
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(blank=True, default='', verbose_name='Текст')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
    photo = models.ImageField(verbose_name='Фото', upload_to='uploads/', blank=True)
    slug = models.SlugField(verbose_name='Url', blank=True, null=True, unique=True)
    class Meta:
        verbose_name = 'Услуги'
        verbose_name_plural = 'Услуга'

    def __str__(self):
        return self.title

    def get_absolute_url(self): #метод get_absolute_url () в наших шаблонах для ссылки на конкретные посты.
        return reverse('service_detail',
                       args=[self.id])


class Portfolio(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Опубликовано')
    )
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    body = models.TextField(blank=True, default='', verbose_name='Текст')
    publish = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name='Статус')
    photo = models.ImageField(upload_to='albums/avatar/', verbose_name='Первая фото', blank=True)
    slug = models.SlugField(verbose_name='Url', blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Наши работы'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return self.title


class PhotoItem(models.Model):
    image = models.ImageField(upload_to='albums/portfolio/', verbose_name='Галерея', blank=True, null=True, unique=True)
    photo = models.ForeignKey(Portfolio, related_name='photoitems', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.photo.id)