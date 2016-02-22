# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothing', '0029_auto_20160117_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='Selling',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('count', models.IntegerField(verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('price', models.FloatField(default=0.0, verbose_name=b'\xe5\x8d\x95\xe4\xbb\xb7')),
                ('good', models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.Good')),
                ('user', models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u9500\u552e\u8bb0\u5f55',
                'verbose_name_plural': '\u9500\u552e\u8bb0\u5f55',
            },
        ),
        migrations.AlterModelOptions(
            name='ad',
            options={'verbose_name': '\u5e7f\u544a', 'verbose_name_plural': '\u5e7f\u544a'},
        ),
        migrations.AlterField(
            model_name='ad',
            name='img',
            field=models.ImageField(upload_to=b'ad/', verbose_name=b'\xe5\xb9\xbf\xe5\x91\x8a\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='count',
            field=models.IntegerField(default=1, verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(verbose_name=b'\xe5\x95\x86\xe5\x93\x81', to='clothing.Good'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL),
        ),
    ]
