# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='num1',
            field=models.CharField(max_length=9, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='num2',
            field=models.CharField(max_length=9, default=1),
            preserve_default=False,
        ),
    ]
