# Generated by Django 3.1 on 2021-11-13 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0007_auto_20211113_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='phone',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
