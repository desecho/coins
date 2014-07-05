# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0002_auto_20140706_0000'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coin',
            options={'ordering': [b'currency', b'series', b'year', b'name'], 'verbose_name': b'\xd0\xbc\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82\xd0\xb0', 'verbose_name_plural': b'\xd0\xbc\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x82\xd1\x8b'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'ordering': [b'name'], 'verbose_name': b'\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd0\xb0', 'verbose_name_plural': b'\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd0\xbd\xd1\x8b'},
        ),
        migrations.AlterModelOptions(
            name='currency',
            options={'ordering': [b'country', b'name'], 'verbose_name': b'\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb6\xd0\xbd\xd0\xb0\xd1\x8f \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd0\xb0', 'verbose_name_plural': b'\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb5\xd0\xb6\xd0\xbd\xd1\x8b\xd0\xb5 \xd0\xb5\xd0\xb4\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x86\xd1\x8b'},
        ),
        migrations.AlterModelOptions(
            name='period',
            options={'ordering': [b'country', b'name'], 'verbose_name': b'\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4', 'verbose_name_plural': b'\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb8\xd0\xbe\xd0\xb4\xd1\x8b'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'ordering': [b'country', b'name'], 'verbose_name': b'\xd1\x81\xd0\xb5\xd1\x80\xd0\xb8\xd1\x8f', 'verbose_name_plural': b'\xd1\x81\xd0\xb5\xd1\x80\xd0\xb8\xd0\xb8'},
        ),
        migrations.AddField(
            model_name='coin',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.RemoveField(
            model_name='coin',
            name='theme',
        ),
    ]
