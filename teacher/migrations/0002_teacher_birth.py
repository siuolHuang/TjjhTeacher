# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='birth',
            field=models.DateField(default=datetime.datetime(2019, 6, 19, 6, 28, 23, 503677, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
