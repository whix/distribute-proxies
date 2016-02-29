# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0006_auto_20151010_1738'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 17, 50, 48, 379000), auto_now_add=True),
            preserve_default=False,
        ),
    ]
