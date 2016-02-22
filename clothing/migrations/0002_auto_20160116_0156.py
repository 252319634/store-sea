# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='major',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='qq',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'QQ\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80', blank=True),
        ),
    ]
