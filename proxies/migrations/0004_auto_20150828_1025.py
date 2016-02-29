# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0003_auto_20150819_1016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxies',
            options={'ordering': ['-add_date']},
        ),
        migrations.AddField(
            model_name='proxies',
            name='website',
            field=models.CharField(default=b'no website', max_length=100),
        ),
        migrations.AlterField(
            model_name='proxies',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
