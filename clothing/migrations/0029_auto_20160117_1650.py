# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0028_auto_20160117_0258'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87')),
            ],
        ),
        migrations.AlterField(
            model_name='good',
            name='tag',
            field=models.ManyToManyField(to='clothing.Tag', null=True, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe', blank=True),
        ),
        migrations.AddField(
            model_name='ad',
            name='good',
            field=models.ForeignKey(to='clothing.Good'),
        ),
    ]
