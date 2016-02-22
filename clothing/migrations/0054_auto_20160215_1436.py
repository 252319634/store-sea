# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0053_auto_20160202_2124'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsku',
            options={'verbose_name': '\u5546\u54c1SKU', 'verbose_name_plural': '\u5546\u54c1SKU'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='recipients',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x94\xb6\xe4\xbb\xb6\xe4\xba\xba'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.GoodSku'),
        ),
        migrations.AlterField(
            model_name='selling',
            name='good',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.GoodSku'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(default=b'', max_length=200, verbose_name=b'\xe5\x9c\xb0\xe5\x9d\x80'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='tel',
            field=models.CharField(default=b'', max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7\xe7\xa0\x81'),
        ),
    ]
