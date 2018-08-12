# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-08-12 05:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20180811_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('deadline', models.CharField(max_length=100)),
                ('dateOfVisit', models.CharField(max_length=100)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=50)),
                ('header', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('poster', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InternJobOpening',
            fields=[
                ('jobopening_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.JobOpening')),
            ],
            bases=('api.jobopening',),
        ),
        migrations.CreateModel(
            name='InternNotification',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Notification')),
            ],
            bases=('api.notification',),
        ),
        migrations.CreateModel(
            name='PlacementJobOpening',
            fields=[
                ('jobopening_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.JobOpening')),
            ],
            bases=('api.jobopening',),
        ),
        migrations.CreateModel(
            name='PlacementNotification',
            fields=[
                ('notification_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Notification')),
            ],
            bases=('api.notification',),
        ),
    ]
