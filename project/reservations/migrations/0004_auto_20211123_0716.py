# Generated by Django 3.2.7 on 2021-11-23 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20211111_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registereduser',
            name='billing_address',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='registereduser',
            name='mailing_address',
            field=models.CharField(max_length=60),
        ),
    ]
