# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 12:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='数据创建时间')),
                ('modifytime', models.DateTimeField(auto_now=True, verbose_name='数据最后修改时间')),
                ('remark', models.TextField(verbose_name='备注')),
                ('href', models.CharField(max_length=200, verbose_name='小说具体链接')),
                ('content', models.TextField(verbose_name='章节具体内容')),
                ('serial_number', models.IntegerField(verbose_name='章节序号')),
            ],
            options={
                'verbose_name_plural': 'Chapters',
                'verbose_name': 'Chapter',
            },
        ),
        migrations.CreateModel(
            name='NovelInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='名称')),
                ('createtime', models.DateTimeField(auto_now_add=True, verbose_name='数据创建时间')),
                ('modifytime', models.DateTimeField(auto_now=True, verbose_name='数据最后修改时间')),
                ('remark', models.TextField(verbose_name='备注')),
                ('avatar', models.CharField(max_length=200, verbose_name='小说图片链接')),
                ('author', models.CharField(max_length=20, verbose_name='小说作者')),
                ('category', models.CharField(max_length=20, verbose_name='小说分类')),
                ('state', models.CharField(max_length=10, verbose_name='更新状态')),
                ('words', models.IntegerField(verbose_name='字数')),
                ('latest_updatetime', models.CharField(max_length=20, verbose_name='最后更新时间')),
                ('latest_chapter', models.CharField(max_length=200, verbose_name='最新章节名')),
                ('website', models.CharField(max_length=200, verbose_name='小说网站')),
                ('novelId', models.CharField(max_length=200, verbose_name='小说ID')),
                ('intro', models.TextField(verbose_name='小说简介')),
            ],
            options={
                'verbose_name_plural': 'Novels',
                'verbose_name': 'Novel',
            },
        ),
        migrations.AddField(
            model_name='chapter',
            name='novelInfo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readnovel.NovelInfo', verbose_name='所属小说'),
        ),
    ]
