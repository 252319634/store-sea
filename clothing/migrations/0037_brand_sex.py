# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0036_auto_20160122_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='sex',
            field=models.SmallIntegerField(default=1, blank=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(1, b'\xe7\x94\xb7\xe5\xbc\x8f'), (0, b'\xe5\xa5\xb3\xe5\xbc\x8f')]),
        ),
    ]
