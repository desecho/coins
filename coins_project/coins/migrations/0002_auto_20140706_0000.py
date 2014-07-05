# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='year',
            field=models.PositiveSmallIntegerField(default=0, verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xb4'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='coin',
            name='years',
        ),
        migrations.DeleteModel(
            name='Year',
        ),
    ]
