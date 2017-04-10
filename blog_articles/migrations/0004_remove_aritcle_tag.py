# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_articles', '0003_auto_20170408_2130'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aritcle',
            name='tag',
        ),
    ]
