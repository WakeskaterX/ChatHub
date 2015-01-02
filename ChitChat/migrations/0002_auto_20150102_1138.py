# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ChitChat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='parent',
            field=models.ForeignKey(to='ChitChat.Message', default=None, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='posted',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 2, 11, 38, 34, 602685), verbose_name='Date Posted'),
            preserve_default=True,
        ),
    ]
