# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='id_good',
            field=models.CharField(max_length=32, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(unique=True, max_length=64),
            preserve_default=True,
        ),
    ]
