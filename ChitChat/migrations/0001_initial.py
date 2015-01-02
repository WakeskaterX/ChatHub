# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=200)),
                ('posted', models.DateTimeField(verbose_name='Date Posted', default=datetime.datetime(2015, 1, 2, 11, 20, 56, 542168))),
                ('linked', models.IntegerField(default=0)),
                ('replies', models.IntegerField(default=0)),
                ('favorites', models.IntegerField(default=0)),
                ('topics', models.CharField(default=None, max_length=25, null=True, blank=True)),
                ('parent', models.ForeignKey(to='ChitChat.Message')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
