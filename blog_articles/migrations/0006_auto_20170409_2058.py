# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_articles', '0005_aritcle_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='modefied_time',
            new_name='modified_time',
        ),
    ]
