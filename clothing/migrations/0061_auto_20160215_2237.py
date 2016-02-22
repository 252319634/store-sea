# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothing', '0060_selling_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True, verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe6\x97\xb6\xe9\x97\xb4', null=True)),
                ('address', models.CharField(max_length=200, verbose_name=b'\xe6\x94\xb6\xe8\xb4\xa7\xe4\xbf\xa1\xe6\x81\xaf')),
                ('total_price', models.FloatField(default=0.0, verbose_name=b'\xe6\x80\xbb\xe9\x87\x91\xe9\xa2\x9d')),
            ],
        ),
        migrations.RemoveField(
            model_name='selling',
            name='address',
        ),
        migrations.RemoveField(
            model_name='selling',
            name='orderid',
        ),
        migrations.RemoveField(
            model_name='selling',
            name='time',
        ),
        migrations.RemoveField(
            model_name='selling',
            name='user',
        ),
        migrations.AddField(
            model_name='order',
            name='selling',
            field=models.ManyToManyField(to='clothing.Selling', verbose_name=b'\xe9\x94\x80\xe5\x94\xae\xe8\xae\xb0\xe5\xbd\x95'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
