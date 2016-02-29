# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0008_remove_domain_add_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='domain',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 27, 17, 20, 49, 182000), auto_now_add=True),
            preserve_default=False,
        ),
    ]
