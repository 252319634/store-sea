# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0056_selling_orderid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='goods',
            new_name='goodsku',
        ),
        migrations.RenameField(
            model_name='selling',
            old_name='good',
            new_name='goodsku',
        ),
        migrations.AlterField(
            model_name='selling',
            name='orderid',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7', blank=True),
        ),
    ]
