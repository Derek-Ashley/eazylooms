# Generated by Django 3.1 on 2021-11-13 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0010_auto_20211113_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]
