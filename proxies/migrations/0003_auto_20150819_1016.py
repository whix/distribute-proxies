# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0002_proxies_add_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proxies',
            options={'ordering': ['proxy']},
        ),
    ]
