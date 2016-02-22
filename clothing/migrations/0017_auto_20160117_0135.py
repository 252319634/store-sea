# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0016_good_artno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10, verbose_name=b'\xe9\xa2\x9c\xe8\x89\xb2')),
            ],
            options={
                'verbose_name': '\u989c\u8272',
                'verbose_name_plural': '\u989c\u8272',
            },
        ),
        migrations.CreateModel(
            name='GoodSku',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('old_price', models.FloatField(default=0.0, verbose_name=b'\xe5\x8e\x9f\xe4\xbb\xb7')),
                ('new_price', models.FloatField(default=0.0, verbose_name=b'\xe7\x8e\xb0\xe4\xbb\xb7')),
                ('num', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('sales', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f')),
                ('color', models.ForeignKey(verbose_name=b'\xe9\xa2\x9c\xe8\x89\xb2', to='clothing.Color')),
            ],
        ),
        migrations.RemoveField(
            model_name='good',
            name='new_price',
        ),
        migrations.RemoveField(
            model_name='good',
            name='num',
        ),
        migrations.RemoveField(
            model_name='good',
            name='old_price',
        ),
        migrations.RemoveField(
            model_name='good',
            name='sales',
        ),
        migrations.RemoveField(
            model_name='good',
            name='size',
        ),
        migrations.AlterField(
            model_name='img',
            name='goodsid',
            field=models.ForeignKey(to='clothing.GoodSku'),
        ),
        migrations.AddField(
            model_name='goodsku',
            name='good',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.Good'),
        ),
        migrations.AddField(
            model_name='goodsku',
            name='image',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', blank=True, to='clothing.Img', null=True),
        ),
        migrations.AddField(
            model_name='goodsku',
            name='size',
            field=models.ForeignKey(verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8', to='clothing.Size'),
        ),
    ]
