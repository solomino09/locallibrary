# Generated by Django 2.0.5 on 2018-05-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20180523_1655'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='libraries',
        ),
        migrations.AddField(
            model_name='book',
            name='libraries',
            field=models.ManyToManyField(help_text='Select the libraries for this book', to='catalog.Libraries'),
        ),
    ]
