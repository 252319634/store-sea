# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0003_auto_20160116_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='discount',
        ),
    ]
