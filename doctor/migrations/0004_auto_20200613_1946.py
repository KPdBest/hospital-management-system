# Generated by Django 2.0 on 2020-06-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_auto_20200613_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='qualification',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
