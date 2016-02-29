# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proxies', '0005_proxies_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('domain', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='proxies',
            name='related_domain',
            field=models.ForeignKey(to='proxies.Domain', null=True),
        ),
    ]
