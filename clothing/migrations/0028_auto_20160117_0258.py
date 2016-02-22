# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0027_goodsku_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='tag',
            field=models.ManyToManyField(to='clothing.Tag', null=True, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
