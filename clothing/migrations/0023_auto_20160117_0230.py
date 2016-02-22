# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0022_auto_20160117_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsku',
            name='image',
        ),
        migrations.AddField(
            model_name='img',
            name='goodsku',
            field=models.ForeignKey(default=0, to='clothing.GoodSku'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'\xe4\xb8\xbb\xe5\x9b\xbe', blank=True),
        ),
    ]
