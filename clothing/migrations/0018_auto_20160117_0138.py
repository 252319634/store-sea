# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0017_auto_20160117_0135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img',
            old_name='goodsid',
            new_name='goodsku',
        ),
        migrations.RemoveField(
            model_name='good',
            name='image',
        ),
        migrations.RemoveField(
            model_name='goodsku',
            name='image',
        ),
        migrations.AddField(
            model_name='img',
            name='good',
            field=models.ForeignKey(default=0, to='clothing.Good'),
            preserve_default=False,
        ),
    ]
