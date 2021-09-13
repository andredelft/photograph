# Generated by Django 3.2.7 on 2021-09-13 09:59

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photograph', '0002_form_enhancements'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='file',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
