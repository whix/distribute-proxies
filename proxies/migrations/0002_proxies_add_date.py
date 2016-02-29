# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxies',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 19, 1, 57, 41, 551268, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
