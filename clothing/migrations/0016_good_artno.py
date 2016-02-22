# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0015_auto_20160117_0002'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='artno',
            field=models.CharField(default=0, max_length=30, verbose_name=b'\xe8\xb4\xa7\xe5\x8f\xb7'),
            preserve_default=False,
        ),
    ]
