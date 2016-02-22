# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0039_good_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='sex',
        ),
    ]
