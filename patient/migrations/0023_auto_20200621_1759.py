# Generated by Django 2.0 on 2020-06-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0022_auto_20200621_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='change_made_by',
        ),
        migrations.AddField(
            model_name='notification',
            name='changes_made_by',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
