# Generated by Django 2.0 on 2020-06-22 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0013_auto_20200621_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='status',
        ),
    ]
