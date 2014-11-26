# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import entropy.mixins


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('short_title', models.CharField(max_length=255, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255)),
                ('enabled', models.BooleanField(default=False, db_index=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(entropy.mixins.BaseSlugMixin, models.Model),
        ),
    ]
