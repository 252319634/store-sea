# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0011_good_attr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='good',
            old_name='attr',
            new_name='attrvalue',
        ),
        migrations.AddField(
            model_name='attrvalue',
            name='attr',
            field=models.ForeignKey(default=1, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x90\x8d', to='clothing.Attr'),
            preserve_default=False,
        ),
    ]
