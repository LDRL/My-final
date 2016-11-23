# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cantidad', models.IntegerField()),
                ('fecha_compra', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('dpi', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('codigo', models.CharField(max_length=7)),
                ('nombre', models.CharField(max_length=30)),
                ('imagen', models.ImageField(null=True, upload_to='fotos', blank=True)),
                ('precio', models.FloatField()),
                ('Existencia', models.IntegerField()),
                ('marca', models.ForeignKey(to='blog.Marca')),
            ],
        ),
        migrations.AddField(
            model_name='compra',
            name='persona',
            field=models.ForeignKey(to='blog.Persona'),
        ),
        migrations.AddField(
            model_name='compra',
            name='productos',
            field=models.ManyToManyField(to='blog.Producto', through='blog.CD'),
        ),
        migrations.AddField(
            model_name='cd',
            name='compra',
            field=models.ForeignKey(to='blog.Compra'),
        ),
        migrations.AddField(
            model_name='cd',
            name='producto',
            field=models.ForeignKey(to='blog.Producto'),
        ),
    ]
