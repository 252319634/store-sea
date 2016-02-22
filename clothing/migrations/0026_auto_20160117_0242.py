# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0025_auto_20160117_0239'),
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
    ]
