# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-18 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FichaMedica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.TextField(max_length=255)),
                ('peso', models.IntegerField()),
                ('animal', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ganaderia.Animal')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vacuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='fichamedica',
            name='genero',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ganaderia.Genero'),
        ),
        migrations.AddField(
            model_name='fichamedica',
            name='vacuna',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ganaderia.Vacuna'),
        ),
        migrations.AddField(
            model_name='animal',
            name='especies',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='ganaderia.Especie'),
        ),
    ]
