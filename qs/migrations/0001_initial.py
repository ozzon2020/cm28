# Generated by Django 3.2 on 2021-04-25 10:01

import common.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThemeQs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Подраздел', max_length=200, verbose_name='Темы вопросов')),
                ('sort', common.fields.OrderField(blank=True, help_text='Порядок сортировки', verbose_name='<>')),
                ('active', models.BooleanField(default=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name_plural': 'Темы вопросов',
                'ordering': ['-sort'],
            },
        ),
        migrations.CreateModel(
            name='Qs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Имя', max_length=250, verbose_name='Имя')),
                ('theme', models.CharField(help_text='О чем вопрос ', max_length=250, verbose_name='Тема вопроса')),
                ('email', models.CharField(max_length=250, verbose_name='E-mail')),
                ('main', models.TextField(help_text='Заданный вопрос', max_length=40000, verbose_name='Вопрос')),
                ('reply', models.TextField(blank=True, help_text='Ответ', max_length=40000, null=True, verbose_name='Ответ')),
                ('created', models.DateTimeField(default=datetime.datetime.now, help_text='Дата Создания', verbose_name='Создание')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('sort', common.fields.OrderField(blank=True, help_text='Порядок сортировки', verbose_name='Порядок сортировки')),
                ('replyoff', models.BooleanField(blank=True, default=False, verbose_name='Ответ')),
                ('active', models.BooleanField(default=True, verbose_name='Статус')),
                ('var', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='qstheme', to='qs.themeqs', verbose_name='Тема')),
            ],
            options={
                'verbose_name_plural': 'Вопрос - Ответ',
                'ordering': ['-created'],
            },
        ),
    ]