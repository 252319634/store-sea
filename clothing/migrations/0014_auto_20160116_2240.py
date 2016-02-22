# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0013_auto_20160116_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attrvalue',
            name='name',
            field=models.CharField(max_length=30, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x80\xbc'),
        ),
    ]
