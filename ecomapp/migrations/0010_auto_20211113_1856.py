# Generated by Django 3.1 on 2021-11-13 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0009_auto_20211113_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='phone',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
