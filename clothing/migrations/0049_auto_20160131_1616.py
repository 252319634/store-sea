# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0048_auto_20160131_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attrvalue',
            name='category',
        ),
        migrations.AddField(
            model_name='category',
            name='attrvalue',
            field=models.ManyToManyField(to='clothing.AttrValue', verbose_name=b'\xe7\xbb\x86\xe8\x8a\x82'),
        ),
    ]
