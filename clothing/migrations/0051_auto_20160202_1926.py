# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0050_auto_20160201_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='desc',
            field=models.TextField(max_length=10000, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
        ),
    ]
