# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0034_auto_20160121_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='price',
            field=models.FloatField(default=0.0, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
    ]
