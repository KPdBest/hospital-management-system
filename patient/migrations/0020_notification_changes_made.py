# Generated by Django 2.0 on 2020-06-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0019_remove_notification_changes_made'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='changes_made',
            field=models.CharField(default='pending', max_length=150),
        ),
    ]
