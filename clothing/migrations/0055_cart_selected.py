# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0054_auto_20160215_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='selected',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xbb\x93\xe7\xae\x97'),
        ),
    ]
