# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0044_auto_20160129_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='sex',
        ),
    ]
