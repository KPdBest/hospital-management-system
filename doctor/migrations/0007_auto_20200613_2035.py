# Generated by Django 2.0 on 2020-06-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_auto_20200613_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='status',
        ),
        migrations.AddField(
            model_name='registration',
            name='previous_exp',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='registration',
            name='qualification',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
