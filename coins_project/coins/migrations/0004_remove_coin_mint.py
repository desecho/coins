# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0003_auto_20140706_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coin',
            name='mint',
        ),
    ]
