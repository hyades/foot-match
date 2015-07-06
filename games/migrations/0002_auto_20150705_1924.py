# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='games',
        ),
        migrations.AddField(
            model_name='match',
            name='game',
            field=models.ForeignKey(to='games.Game', null=True),
            preserve_default=True,
        ),
    ]
