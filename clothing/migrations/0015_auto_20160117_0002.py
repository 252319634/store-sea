# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0014_auto_20160116_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('index', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
            options={
                'verbose_name': '\u54c1\u724c',
                'verbose_name_plural': '\u54c1\u724c',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x88\x86\xe7\xb1\xbb')),
                ('index', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
            options={
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8')),
                ('index', models.IntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f')),
            ],
            options={
                'verbose_name': '\u5c3a\u5bf8',
                'verbose_name_plural': '\u5c3a\u5bf8',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe')),
            ],
            options={
                'verbose_name': '\u6807\u7b7e',
                'verbose_name_plural': '\u6807\u7b7e',
            },
        ),
        migrations.AlterModelOptions(
            name='attrvalue',
            options={'ordering': ('attr__name',), 'verbose_name': '\u5c5e\u6027\u503c', 'verbose_name_plural': '\u5c5e\u6027\u503c'},
        ),
        migrations.AddField(
            model_name='good',
            name='brand',
            field=models.ForeignKey(default=0, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c', to='clothing.Brand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='good',
            name='category',
            field=models.ForeignKey(default=0, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='clothing.Category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='good',
            name='size',
            field=models.ForeignKey(default=0, verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8', to='clothing.Size'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='good',
            name='tag',
            field=models.ManyToManyField(to='clothing.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
