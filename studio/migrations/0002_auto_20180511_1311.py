# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-11 10:11
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Project description'),
        ),
    ]
