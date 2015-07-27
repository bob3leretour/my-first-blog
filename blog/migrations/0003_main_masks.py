# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20150723_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_masks',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.TextField()),
                ('exemple', models.ForeignKey(to='blog.Post', default=1)),
            ],
        ),
    ]
