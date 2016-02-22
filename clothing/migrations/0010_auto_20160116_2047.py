# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0009_auto_20160116_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x90\x8d\xe7\xa7\xb0')),
            ],
            options={
                'verbose_name': '\u5c5e\u6027\u540d\u79f0',
                'verbose_name_plural': '\u5c5e\u6027\u540d\u79f0',
            },
        ),
        migrations.CreateModel(
            name='AttrValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\xb1\x9e\xe6\x80\xa7\xe5\x80\xbc')),
            ],
            options={
                'verbose_name': '\u5c5e\u6027\u503c',
                'verbose_name_plural': '\u5c5e\u6027\u503c',
            },
        ),
        migrations.RemoveField(
            model_name='good',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='good',
            name='category',
        ),
        migrations.RemoveField(
            model_name='good',
            name='size',
        ),
        migrations.RemoveField(
            model_name='good',
            name='tag',
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
