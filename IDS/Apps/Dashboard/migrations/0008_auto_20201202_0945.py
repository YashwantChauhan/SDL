# Generated by Django 2.2.4 on 2020-12-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0007_remove_files_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='files',
            name='describe',
            field=models.TextField(max_length=200),
        ),
    ]
