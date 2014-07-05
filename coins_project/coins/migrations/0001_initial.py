# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Coin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.CharField(max_length=255, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb0\xd0\xbb')),
                ('image1', models.ImageField(upload_to=b'img', null=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 1', blank=True)),
                ('image2', models.ImageField(upload_to=b'img', null=True, verbose_name=b'\xd0\xb8\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 2', blank=True)),
                ('theme', models.CharField(max_length=255, null=True, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0', blank=True)),
                ('mint', models.CharField(max_length=255, null=True, verbose_name=b'\xd0\xbc\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb4\xd0\xb2\xd0\xbe\xd1\x80', blank=True)),
                ('material', models.CharField(max_length=255, null=True, verbose_name=b'\xd0\xbc\xd0\xb0\xd1\x82\xd0\xb5\xd1\x80\xd0\xb8\xd0\xb0\xd0\xbb', blank=True)),
                ('comment', models.CharField(max_length=255, null=True, verbose_name=b'\xd0\xba\xd0\xbe\xd0\xbc\xd0\xbc\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0\xd1\x80\xd0\xb8\xd0\xb9', blank=True)),
                ('user', models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': b'\xd0\xbc\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82\xd0\xb0',
                'verbose_name_plural': b'\xd0\xbc\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82\xd1\x8b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'verbose_name': b'\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0',
                'verbose_name_plural': b'\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd1\x8b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('country', models.ForeignKey(verbose_name=b'\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0', to='coins.Country')),
            ],
            options={
                'verbose_name': b'\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb6\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0',
                'verbose_name_plural': b'\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb6\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coin',
            name='currency',
            field=models.ForeignKey(verbose_name=b'\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb6\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0', to='coins.Currency'),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('country', models.ForeignKey(verbose_name=b'\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0', to='coins.Country')),
            ],
            options={
                'verbose_name': b'\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4',
                'verbose_name_plural': b'\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4\xd1\x8b',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coin',
            name='period',
            field=models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4', blank=True, to='coins.Period', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('country', models.ForeignKey(verbose_name=b'\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0', to='coins.Country')),
            ],
            options={
                'verbose_name': b'\xd1\x81\xd0\xb5\xd1\x80\xd0\xb8\xd1\x8f',
                'verbose_name_plural': b'\xd1\x81\xd0\xb5\xd1\x80\xd0\xb8\xd0\xb8',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coin',
            name='series',
            field=models.ForeignKey(verbose_name=b'\xd1\x81\xd0\xb5\xd1\x80\xd0\xb8\xd1\x8f', blank=True, to='coins.Series', null=True),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.PositiveSmallIntegerField(verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xb4')),
            ],
            options={
                'verbose_name': b'\xd0\xb3\xd0\xbe\xd0\xb4',
                'verbose_name_plural': b'\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='coin',
            name='years',
            field=models.ManyToManyField(to='coins.Year', verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xb4\xd0\xb0'),
            preserve_default=True,
        ),
    ]
