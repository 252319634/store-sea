# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0032_good_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='sales_month',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9c\xac\xe6\x9c\x88\xe9\x94\x80\xe9\x87\x8f'),
        ),
    ]
