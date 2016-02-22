# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0040_remove_tag_sex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat2',
            name='father',
        ),
        migrations.RemoveField(
            model_name='category',
            name='father',
        ),
        migrations.DeleteModel(
            name='Cat1',
        ),
        migrations.DeleteModel(
            name='Cat2',
        ),
    ]
