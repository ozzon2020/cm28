# Generated by Django 3.2 on 2021-04-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_auto_20210425_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='pages',
            field=models.ManyToManyField(blank=True, null=True, to='content.Section', verbose_name='list of sites'),
        ),
    ]
