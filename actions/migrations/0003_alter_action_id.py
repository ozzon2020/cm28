# Generated by Django 3.2 on 2021-04-25 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0002_alter_action_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
