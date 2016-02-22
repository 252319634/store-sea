# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0004_remove_goods_discount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('old_price', models.FloatField(default=0.0, verbose_name=b'\xe5\x8e\x9f\xe4\xbb\xb7')),
                ('new_price', models.FloatField(default=0.0, verbose_name=b'\xe7\x8e\xb0\xe4\xbb\xb7')),
                ('desc', models.CharField(max_length=100, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('sales', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f')),
                ('num', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('brand', models.ForeignKey(verbose_name=b'\xe5\x93\x81\xe7\x89\x8c', to='clothing.Brand')),
                ('category', models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='clothing.Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='goods',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='category',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='image',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='size',
        ),
        migrations.RemoveField(
            model_name='goods',
            name='tag',
        ),
        migrations.AlterField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(to='clothing.Good'),
        ),
        migrations.AlterField(
            model_name='img',
            name='goodsid',
            field=models.ForeignKey(to='clothing.Good'),
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.AddField(
            model_name='good',
            name='image',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', to='clothing.Img'),
        ),
        migrations.AddField(
            model_name='good',
            name='size',
            field=models.ManyToManyField(to='clothing.Size', verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8'),
        ),
        migrations.AddField(
            model_name='good',
            name='tag',
            field=models.ManyToManyField(to='clothing.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
    ]
