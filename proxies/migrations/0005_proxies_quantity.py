# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0004_auto_20150828_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='proxies',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
