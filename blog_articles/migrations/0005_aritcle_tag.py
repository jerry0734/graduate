# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_articles', '0004_remove_aritcle_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='aritcle',
            name='tag',
            field=models.ManyToManyField(to='blog_articles.Tag', blank=True),
        ),
    ]
