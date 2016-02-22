# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0012_auto_20160116_2052'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attr',
            options={'ordering': ('name',), 'verbose_name': '\u5c5e\u6027', 'verbose_name_plural': '\u5c5e\u6027'},
        ),
        migrations.AlterField(
            model_name='attrvalue',
            name='name',
            field=models.CharField(unique=True, max_length=30, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x80\xbc'),
        ),
    ]
