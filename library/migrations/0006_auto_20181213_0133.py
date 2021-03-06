# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-12 22:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_auto_20181213_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date',
            field=models.DateField(verbose_name='Дата рождения автора'),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(max_length=100, verbose_name='Фамилия автора'),
        ),
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateField(verbose_name='Дата издания книги в формате гг-мм-дд'),
        ),
        migrations.AlterField(
            model_name='book',
            name='info',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Расскажите нам свое мнение о книге'),
        ),
    ]
