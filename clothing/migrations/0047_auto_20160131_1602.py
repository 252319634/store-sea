# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0046_auto_20160129_2158'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodsku',
            options={'verbose_name': '\u5546\u54c1\u7ec6\u8282', 'verbose_name_plural': '\u5546\u54c1\u7ec6\u8282'},
        ),
        migrations.AddField(
            model_name='attr',
            name='category',
            field=models.ManyToManyField(to='clothing.Category', verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb'),
        ),
    ]
