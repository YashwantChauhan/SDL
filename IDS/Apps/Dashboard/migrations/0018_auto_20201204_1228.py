# Generated by Django 2.2.4 on 2020-12-04 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0017_auto_20201204_1142'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='Result',
            new_name='result',
        ),
    ]