# Generated by Django 2.2.4 on 2020-12-01 16:25

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0003_auto_20201201_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='user_name',
            field=models.TextField(default=django.contrib.auth.models.User, max_length=20),
        ),
    ]
