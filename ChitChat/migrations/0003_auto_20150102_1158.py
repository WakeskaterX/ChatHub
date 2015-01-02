# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('ChitChat', '0002_auto_20150102_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='posted',
            field=models.DateTimeField(verbose_name='Date Posted', default=datetime.datetime(2015, 1, 2, 11, 58, 45, 824963)),
            preserve_default=True,
        ),
    ]
