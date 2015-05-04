# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('router_api', '0002_auto_20150415_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=52)),
            ],
        ),
        migrations.AlterField(
            model_name='routecount',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='routecount',
            name='vpn',
            field=models.ForeignKey(related_name='numroutes', to='router_api.Vpn'),
        ),
        migrations.AlterField(
            model_name='router',
            name='updated_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='router',
            name='vendor',
            field=models.ForeignKey(related_name='vendor', default=1, to='router_api.Vendor'),
            preserve_default=False,
        ),
    ]
