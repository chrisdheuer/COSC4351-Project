# Generated by Django 3.2.7 on 2021-11-28 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0009_rename_num_guests_reservation_number_of_guests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restauranttable',
            old_name='table_num',
            new_name='id',
        ),
    ]