# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0003_auto_20170329_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrfid',
            name='rfid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userdetails.RfidCar'),
        ),
    ]