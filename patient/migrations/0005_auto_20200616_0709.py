# Generated by Django 2.0 on 2020-06-16 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_remove_registration_medical_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='registration',
            new_name='registrationp',
        ),
    ]
