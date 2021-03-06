# Generated by Django 3.1 on 2021-11-13 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapp', '0006_contactform'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactform',
            options={'verbose_name_plural': 'Contact'},
        ),
        migrations.AddField(
            model_name='contactform',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='message',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='name',
            field=models.CharField(help_text='Name of the sender', max_length=200),
        ),
    ]
