# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0035_good_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='name',
            field=models.CharField(max_length=100, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
    ]
