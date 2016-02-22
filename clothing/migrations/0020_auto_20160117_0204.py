# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0019_auto_20160117_0201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.OneToOneField(null=True, blank=True, to='clothing.Img', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='goodsku',
            name='image',
            field=models.OneToOneField(null=True, blank=True, to='clothing.Img', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87'),
        ),
    ]
