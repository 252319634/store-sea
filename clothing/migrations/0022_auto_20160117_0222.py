# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0021_auto_20160117_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AlterField(
            model_name='goodsku',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
    ]
