# Generated by Django 3.2.7 on 2021-11-27 23:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20211127_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_num', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('num_guests', models.IntegerField()),
                ('reservation_time', models.DateTimeField()),
                ('reserved_table_num', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.restauranttable')),
            ],
        ),
    ]
