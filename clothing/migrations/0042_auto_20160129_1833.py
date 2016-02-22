# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0041_auto_20160129_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='price',
        ),
        migrations.RemoveField(
            model_name='good',
            name='sales',
        ),
        migrations.RemoveField(
            model_name='good',
            name='sales_month',
        ),
    ]
