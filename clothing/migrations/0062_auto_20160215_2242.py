# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0061_auto_20160215_2237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='selling',
        ),
        migrations.AddField(
            model_name='selling',
            name='order',
            field=models.ForeignKey(default=1, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7', to='clothing.Order'),
            preserve_default=False,
        ),
    ]
