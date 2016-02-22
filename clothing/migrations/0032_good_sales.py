# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0031_category_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='sales',
            field=models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f'),
        ),
    ]
