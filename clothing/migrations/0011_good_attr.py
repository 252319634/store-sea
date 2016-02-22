# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0010_auto_20160116_2047'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='attr',
            field=models.ManyToManyField(to='clothing.AttrValue', verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7'),
        ),
    ]
