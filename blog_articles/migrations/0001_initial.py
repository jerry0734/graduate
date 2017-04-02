# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aritcle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='文章标题', max_length=70, help_text='标题')),
                ('body', models.TextField(verbose_name='正文', help_text='请编写你的文章')),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.CharField(default='d', verbose_name='发布状态', choices=[('d', '草稿'), ('p', '发布')], max_length=1)),
                ('abstract', models.CharField(verbose_name='文章摘要', null=True, blank=True, max_length=50, help_text='摘要，可填选项')),
                ('reading', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='赞')),
                ('top', models.BooleanField(default=False, verbose_name='置顶')),
            ],
            options={
                'ordering': ['-modified_time'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='分类名', max_length=20)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('modefied_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.AddField(
            model_name='aritcle',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, null=True, to='blog_articles.Category', verbose_name='分类'),
        ),
    ]
