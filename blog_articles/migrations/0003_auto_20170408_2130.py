# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_articles', '0002_auto_20170406_2144'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name_plural': '标签'},
        ),
        migrations.RemoveField(
            model_name='aritcle',
            name='top',
        ),
        migrations.AddField(
            model_name='aritcle',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aritcle',
            name='tag',
            field=models.ManyToManyField(to='blog_articles.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, default='python'),
            preserve_default=False,
        ),
    ]
