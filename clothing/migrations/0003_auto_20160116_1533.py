# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothing', '0002_auto_20160116_0156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x93\x81\xe7\x89\x8c')),
                ('index', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x88\x86\xe7\xb1\xbb')),
                ('index', models.SmallIntegerField(default=1, verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('old_price', models.FloatField(default=0.0, verbose_name=b'\xe5\x8e\x9f\xe4\xbb\xb7')),
                ('new_price', models.FloatField(default=0.0, verbose_name=b'\xe7\x8e\xb0\xe4\xbb\xb7')),
                ('discount', models.FloatField(default=1, verbose_name=b'\xe6\x8a\x98\xe6\x89\xa3')),
                ('desc', models.CharField(max_length=100, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
                ('sales', models.IntegerField(default=0, verbose_name=b'\xe9\x94\x80\xe9\x87\x8f')),
                ('num', models.IntegerField(default=0, verbose_name=b'\xe5\xba\x93\xe5\xad\x98')),
                ('brand', models.ForeignKey(verbose_name=b'\xe5\x93\x81\xe7\x89\x8c', to='clothing.Brand')),
                ('category', models.ForeignKey(verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb', to='clothing.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img', models.ImageField(upload_to=b'', verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87')),
                ('index', models.SmallIntegerField(verbose_name=b'\xe6\x8e\x92\xe5\xba\x8f')),
                ('goodsid', models.ForeignKey(to='clothing.Goods')),
            ],
            options={
                'verbose_name': '\u5546\u54c1\u56fe\u7247',
                'verbose_name_plural': '\u5546\u54c1\u56fe\u7247',
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
                'ordering': ['index'],
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
        migrations.AddField(
            model_name='goods',
            name='image',
            field=models.ForeignKey(verbose_name=b'\xe5\x9b\xbe\xe7\x89\x87', to='clothing.Img'),
        ),
        migrations.AddField(
            model_name='goods',
            name='size',
            field=models.ManyToManyField(to='clothing.Size', verbose_name=b'\xe5\xb0\xba\xe5\xaf\xb8'),
        ),
        migrations.AddField(
            model_name='goods',
            name='tag',
            field=models.ManyToManyField(to='clothing.Tag', verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(to='clothing.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
