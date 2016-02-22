# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0065_auto_20160220_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'ordering': ['-view'], 'verbose_name': '\u5546\u54c1', 'verbose_name_plural': '\u5546\u54c1'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='view_history',
            field=models.CommaSeparatedIntegerField(default=b'', max_length=10, null=True, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe8\xae\xb0\xe5\xbd\x95'),
        ),
        migrations.AlterField(
            model_name='good',
            name='view',
            field=models.IntegerField(default=0, null=True, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe9\x87\x8f'),
        ),
    ]
