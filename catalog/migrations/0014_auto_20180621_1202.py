# Generated by Django 2.0.5 on 2018-06-21 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0013_libraries_borrower'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libraries',
            old_name='borrower',
            new_name='library',
        ),
    ]
