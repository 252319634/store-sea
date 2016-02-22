# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0043_auto_20160129_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='prices',
            field=models.CharField(default=b'0', max_length=20, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc'),
        ),
    ]
