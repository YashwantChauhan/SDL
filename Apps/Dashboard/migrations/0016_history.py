# Generated by Django 2.2.4 on 2020-12-04 05:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Dashboard', '0015_recommend_activated'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('hist_id', models.AutoField(primary_key=True, serialize=False)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Results', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('recommendations', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]