# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cpu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('utilization', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Interface',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=52)),
                ('description', models.CharField(max_length=200)),
                ('input_bytes', models.IntegerField(default=0)),
                ('output_bytes', models.IntegerField(default=0)),
                ('discards', models.IntegerField(default=0)),
                ('errors', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('utilization', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Router',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('updated_at', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vpn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('import_target', models.CharField(max_length=52)),
                ('route_target', models.CharField(max_length=52)),
                ('num_routes', models.IntegerField(default=0)),
                ('router', models.ForeignKey(related_name='vpns', to='router_api.Router')),
            ],
        ),
        migrations.AddField(
            model_name='memory',
            name='router',
            field=models.ForeignKey(related_name='memory', to='router_api.Router'),
        ),
        migrations.AddField(
            model_name='interface',
            name='router',
            field=models.ForeignKey(related_name='interfaces', to='router_api.Router'),
        ),
        migrations.AddField(
            model_name='cpu',
            name='router',
            field=models.ForeignKey(related_name='cpu', to='router_api.Router'),
        ),
    ]
