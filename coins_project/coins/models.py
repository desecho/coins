# -*- coding: utf8 -*-
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField('название', max_length=255, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'страна'
        verbose_name_plural = 'страны'


class Currency(models.Model):
    name = models.CharField('название', max_length=255)
    country = models.ForeignKey(Country, verbose_name='страна')

    def __unicode__(self):
        return '%s (%s)' % (self.name, unicode(self.country))

    class Meta:
        ordering = ['country', 'name']
        verbose_name = 'денежная единица'
        verbose_name_plural = 'денежные единицы'


class Series(models.Model):
    name = models.CharField('название', max_length=255)
    country = models.ForeignKey(Country, verbose_name='страна')

    def __unicode__(self):
        return '%s (%s)' % (self.name, unicode(self.country))

    class Meta:
        ordering = ['country', 'name']
        verbose_name = 'серия'
        verbose_name_plural = 'серии'


class Period(models.Model):
    name = models.CharField('название', max_length=255)
    country = models.ForeignKey(Country, verbose_name='страна')

    def __unicode__(self):
        return '%s (%s)' % (self.name, unicode(self.country))

    class Meta:
        ordering = ['country', 'name']
        verbose_name = 'период'
        verbose_name_plural = 'периоды'


class Coin(models.Model):
    user = models.ForeignKey(User, verbose_name='пользователь')
    value = models.CharField('номинал', max_length=255)
    currency = models.ForeignKey(Currency, verbose_name='денежная единица')
    name = models.CharField('название', max_length=255, null=True, blank=True)
    year = models.PositiveSmallIntegerField('год', null=True, blank=True)
    image1 = models.ImageField('изображение 1', upload_to=settings.UPLOAD_DIR, null=True, blank=True)
    image2 = models.ImageField('изображение 2', upload_to=settings.UPLOAD_DIR, null=True, blank=True)
    series = models.ForeignKey(Series, verbose_name='серия', null=True, blank=True)
    period = models.ForeignKey(Period, verbose_name='период', null=True, blank=True)
    material = models.CharField('материал', max_length=255, null=True, blank=True)
    comment = models.CharField('комментарий', max_length=255, null=True, blank=True)

    def __unicode__(self):
        name = '%s %s' % (self.value, unicode(self.currency))
        if self.year is not None:
            name += ' - %d' % self.year
        if self.name is not None:
            name += ' - %s' % self.name
        if self.series is not None:
            name += ' - %s' % self.series.name
        return name

    class Meta:
        ordering = ['currency', 'series', 'year', 'name']
        verbose_name = 'монета'
        verbose_name_plural = 'монеты'
