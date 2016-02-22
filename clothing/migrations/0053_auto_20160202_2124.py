# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0052_auto_20160202_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='details',
            field=tinymce.models.HTMLField(default=1, max_length=10000, verbose_name=b'\xe8\xaf\xa6\xe6\x83\x85'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='good',
            name='desc',
            field=models.CharField(max_length=200, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b'),
        ),
    ]
