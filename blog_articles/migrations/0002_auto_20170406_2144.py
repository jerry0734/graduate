# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutme',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('blog_name', models.CharField(verbose_name='博客名称', max_length=50)),
                ('admin_email', models.EmailField(max_length=254)),
                ('other', models.TextField()),
            ],
            options={
                'verbose_name_plural': '关于博客',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='aritcle',
            options={'ordering': ['-modified_time'], 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': '分类'},
        ),
    ]
