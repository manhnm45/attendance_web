# Generated by Django 2.2 on 2024-05-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='avata',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='employees',
            name='file_image',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
