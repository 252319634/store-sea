# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0047_auto_20160131_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attr',
            name='category',
        ),
        migrations.AddField(
            model_name='attrvalue',
            name='category',
            field=models.ManyToManyField(to='clothing.Category', verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb'),
        ),
    ]
