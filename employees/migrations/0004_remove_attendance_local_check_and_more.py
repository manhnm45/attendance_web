# Generated by Django 5.0.6 on 2024-05-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='local_check',
        ),
        migrations.AddField(
            model_name='attendance',
            name='location_check',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
