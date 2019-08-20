# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-20 18:19
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0002_auto_20190820_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cadastro',
            options={'ordering': ['nome_completo']},
        ),
        migrations.AddField(
            model_name='cadastro',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='codigo',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
