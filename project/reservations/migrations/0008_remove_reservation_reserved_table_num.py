# Generated by Django 3.2.7 on 2021-11-27 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0007_auto_20211127_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reserved_table_num',
        ),
    ]
