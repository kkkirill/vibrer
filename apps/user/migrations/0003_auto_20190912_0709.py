# Generated by Django 2.2.4 on 2019-09-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('user', '0002_user_followers_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
