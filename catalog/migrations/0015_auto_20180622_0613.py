# Generated by Django 2.0.5 on 2018-06-22 06:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0014_auto_20180621_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libraries',
            name='library',
        ),
        migrations.AddField(
            model_name='libraries',
            name='libraries',
            field=models.ManyToManyField(help_text='Select Users for this library', to=settings.AUTH_USER_MODEL),
        ),
    ]
