# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0033_good_sales_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa4\xa7\xe7\xb1\xbb')),
                ('sex', models.SmallIntegerField(default=1, blank=True, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', choices=[(1, b'\xe7\x94\xb7\xe5\xbc\x8f'), (0, b'\xe5\xa5\xb3\xe5\xbc\x8f')])),
            ],
            options={
                'verbose_name': '\u4e00\u7ea7\u5206\u7c7b',
                'verbose_name_plural': '\u4e00\u7ea7\u5206\u7c7b',
            },
        ),
        migrations.CreateModel(
            name='Cat2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\xa4\xa7\xe7\xb1\xbb')),
                ('father', models.ForeignKey(verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe5\xa4\xa7\xe7\xb1\xbb', to='clothing.Cat1')),
            ],
            options={
                'verbose_name': '\u4e8c\u7ea7\u5206\u7c7b',
                'verbose_name_plural': '\u4e8c\u7ea7\u5206\u7c7b',
            },
        ),
        migrations.AlterField(
            model_name='good',
            name='image',
            field=models.ImageField(upload_to=b'%Y%m', null=True, verbose_name=b'\xe4\xb8\xbb\xe5\x9b\xbe', blank=True),
        ),
        migrations.AlterField(
            model_name='goodsku',
            name='image',
            field=models.ImageField(upload_to=b'%Y%m', null=True, verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
        migrations.AddField(
            model_name='category',
            name='father',
            field=models.ForeignKey(default=1, verbose_name=b'\xe6\x89\x80\xe5\xb1\x9e\xe4\xba\x8c\xe7\xba\xa7\xe5\x88\x86\xe7\xb1\xbb', to='clothing.Cat2'),
            preserve_default=False,
        ),
    ]
