# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-12 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20160912_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelisting',
            name='applicant_image',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
