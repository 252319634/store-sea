# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0064_auto_20160216_0054'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['-sales'], 'verbose_name': '\u5546\u54c1', 'verbose_name_plural': '\u5546\u54c1'},
        ),
        migrations.AddField(
            model_name='good',
            name='view',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f'),
        ),
    ]
