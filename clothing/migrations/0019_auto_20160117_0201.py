# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0018_auto_20160117_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='good',
        ),
        migrations.RemoveField(
            model_name='img',
            name='goodsku',
        ),
        migrations.RemoveField(
            model_name='img',
            name='index',
        ),
        migrations.AddField(
            model_name='good',
            name='image',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True, to='clothing.Img', null=True),
        ),
        migrations.AddField(
            model_name='goodsku',
            name='image',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True, to='clothing.Img', null=True),
        ),
    ]
