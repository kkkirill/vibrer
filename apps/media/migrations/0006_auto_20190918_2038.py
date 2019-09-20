# Generated by Django 2.2.4 on 2019-09-18 20:38

import django.core.validators
from django.db import migrations, models
import utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20190909_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='explicit',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(upload_to='', validators=[utils.validators.validate_audio_file_extension, utils.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(default=None, upload_to='', validators=[django.core.validators.validate_image_file_extension, utils.validators.validate_file_size]),
        ),
    ]