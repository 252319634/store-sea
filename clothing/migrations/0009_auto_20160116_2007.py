# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0008_auto_20160116_1949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': '\u54c1\u724c', 'verbose_name_plural': '\u54c1\u724c'},
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': '\u8d2d\u7269\u8f66', 'verbose_name_plural': '\u8d2d\u7269\u8f66'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '\u5206\u7c7b', 'verbose_name_plural': '\u5206\u7c7b'},
        ),
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': '\u5546\u54c1', 'verbose_name_plural': '\u5546\u54c1'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name': '\u5c3a\u5bf8', 'verbose_name_plural': '\u5c3a\u5bf8'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237'},
        ),
        migrations.RemoveField(
            model_name='good',
            name='size',
        ),
        migrations.AddField(
            model_name='good',
            name='size',
            field=models.ForeignKey(default=1, verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8', to='clothing.Size'),
            preserve_default=False,
        ),
    ]
