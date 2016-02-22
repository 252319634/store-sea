# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0024_auto_20160117_0237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsku',
            name='image',
        ),
        migrations.AddField(
            model_name='goodsku',
            name='image',
            field=models.ManyToManyField(to='clothing.Img', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
    ]
