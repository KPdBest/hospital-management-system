# Generated by Django 2.0 on 2020-06-21 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0024_auto_20200621_1759'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='change_made_by',
            new_name='changes_made_by',
        ),
    ]
