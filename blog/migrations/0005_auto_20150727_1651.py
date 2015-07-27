# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_for_mainpagedisplay'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_category',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='main_masks',
            name='exemple',
        ),
        migrations.DeleteModel(
            name='Main_masks',
        ),
        migrations.AddField(
            model_name='post',
            name='main_category',
            field=models.ForeignKey(default=1, to='blog.Main_category'),
        ),
    ]
