# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_main_masks'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='for_mainpagedisplay',
            field=models.BooleanField(default=False),
        ),
    ]
