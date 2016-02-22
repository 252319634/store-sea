# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0062_auto_20160215_2242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '\u8ba2\u5355', 'verbose_name_plural': '\u8ba2\u5355'},
        ),
        migrations.AddField(
            model_name='order',
            name='orderid',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95\xe5\x8f\xb7'),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe4\xbf\xa1\xe6\x81\xaf'),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0.0, null=True, verbose_name=b'\xe6\x80\xbb\xe9\x87\x91\xe9\xa2\x9d'),
        ),
    ]
