# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0004_remove_coin_mint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='year',
            field=models.PositiveSmallIntegerField(null=True, verbose_name=b'\xd0\xb3\xd0\xbe\xd0\xb4', blank=True),
        ),
    ]
