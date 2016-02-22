# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0042_auto_20160129_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='nums',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98'),
        ),
        migrations.AddField(
            model_name='good',
            name='prices',
            field=models.FloatField(default=0.0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
        migrations.AddField(
            model_name='good',
            name='sales',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f'),
        ),
    ]
