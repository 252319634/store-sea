# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0058_selling_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selling',
            name='time',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe6\x97\xb6\xe9\x97\xb4', null=True),
        ),
    ]
