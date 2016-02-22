# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0020_auto_20160117_0204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img',
            old_name='img',
            new_name='url',
        ),
    ]
