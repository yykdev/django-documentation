# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-05 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('introduction_to_models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='ManuFacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='shirt_size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], help_text='남자는 L 쓰세요', max_length=1),
        ),
        migrations.AddField(
            model_name='car',
            name='manfacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='introduction_to_models.ManuFacturer'),
        ),
    ]