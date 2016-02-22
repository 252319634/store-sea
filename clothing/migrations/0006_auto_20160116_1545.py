# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0005_auto_20160116_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True, to='clothing.Img'),
        ),
    ]
