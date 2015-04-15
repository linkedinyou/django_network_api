# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('router_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RouteCount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='vpn',
            name='num_routes',
        ),
        migrations.AlterField(
            model_name='cpu',
            name='router',
            field=models.ForeignKey(related_name='cpus', to='router_api.Router'),
        ),
        migrations.AlterField(
            model_name='memory',
            name='router',
            field=models.ForeignKey(related_name='memorys', to='router_api.Router'),
        ),
        migrations.AddField(
            model_name='routecount',
            name='vpn',
            field=models.ForeignKey(related_name='num_routes', to='router_api.Vpn'),
        ),
    ]
