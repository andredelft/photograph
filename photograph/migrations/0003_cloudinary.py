# Generated by Django 3.2.7 on 2021-09-13 12:51

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photograph', '0002_form_enhancements'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='name',
        ),
        migrations.AlterField(
            model_name='collection',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='description',
            field=models.TextField(blank=True, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
