# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0009_domain_add_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proxies',
            name='quantity',
        ),
    ]
