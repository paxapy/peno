# coding=utf-8
from django.db import models

from cms.models import CMSPlugin
from pyuploadcare.dj import ImageField


class Post(models.Model):
    title = models.CharField(u'Название', max_length=142)
    subtitle = models.CharField(u'Подзаголовок', max_length=142, blank=True)
    text = models.TextField(u'Текст')
    image = ImageField(verbose_name=u'Картинка', manual_crop='640x480')

    class Meta:
        verbose_name = u'Запись'
        verbose_name_plural = u'Записи'

    def __unicode__(self):
        return self.title


class Image(CMSPlugin):
    FLOATING_NONE = 'none'
    FLOATING_LEFT = 'left'
    FLOATING_RIGHT = 'right'
    FLOATING_CHOICES = (
        (FLOATING_NONE, u'Нет'),
        (FLOATING_LEFT, u'Слева'),
        (FLOATING_RIGHT, u'Справа'),
    )
    ALIGNMENT_CENTER = 'center'
    ALIGNMENT_LEFT = 'left'
    ALIGNMENT_RIGHT = 'right'
    ALIGNMENT_CHOICES = (
        (ALIGNMENT_CENTER, u'Центр'),
        (ALIGNMENT_LEFT, u'Левый край'),
        (ALIGNMENT_RIGHT, u'Правый край'),
    )
    src = ImageField(verbose_name=u'Картинка', manual_crop='640x480')
    floating = models.CharField(
        u'Обтекание', max_length=5, choices=FLOATING_CHOICES, default=FLOATING_NONE)
    alignment = models.CharField(
        u'Расположение', max_length=6, choices=ALIGNMENT_CHOICES, default=ALIGNMENT_CENTER)
    padding = models.PositiveIntegerField(u'Отступ', default=20)
    width = models.PositiveIntegerField(u'Ширина', default=640)
    height = models.PositiveIntegerField(u'Высота', default=640)