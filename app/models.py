# coding=utf-8
from django.db import models


class Post(models.Model):
    title = models.CharField(u'Название', max_length=142)
    subtitle = models.CharField(u'Подзаголовок', max_length=142, blank=True)
    text = models.TextField(u'Текст')
    image = models.ImageField(u'Картинка', upload_to='images')

    class Meta:
        verbose_name = u'Запись'
        verbose_name_plural = u'Записи'