# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0007_domain_add_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domain',
            name='add_date',
        ),
    ]
