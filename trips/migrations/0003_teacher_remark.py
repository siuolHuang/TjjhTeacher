# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='remark',
            field=models.TextField(blank=True),
        ),
    ]
