# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_pategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='pategory',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
