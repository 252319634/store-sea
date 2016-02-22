# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0059_auto_20160215_1755'),
    ]

    operations = [
        migrations.AddField(
            model_name='selling',
            name='address',
            field=models.CharField(default='', max_length=200, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe4\xbf\xa1\xe6\x81\xaf'),
            preserve_default=False,
        ),
    ]
