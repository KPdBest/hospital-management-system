# Generated by Django 2.0 on 2020-06-19 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_auto_20200619_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='doct',
            new_name='doct_key',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='pt',
            new_name='patient',
        ),
    ]
