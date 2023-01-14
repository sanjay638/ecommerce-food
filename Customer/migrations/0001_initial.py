# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2020-10-09 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Owner', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addtocard_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quality', models.IntegerField()),
                ('day', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('requeststatus', models.CharField(default='PROCESS', max_length=300)),
                ('salesid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Owner.AdminModel')),
            ],
        ),
        migrations.CreateModel(
            name='Feeback_Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('productname', models.CharField(max_length=50)),
                ('ratings', models.CharField(max_length=10)),
                ('feedback', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=300)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('mobilenumber', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='addtocard_model',
            name='userid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.UserRegistration'),
        ),
    ]