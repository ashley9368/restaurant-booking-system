# Generated by Django 4.2.17 on 2024-12-15 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_system', '0003_tablebooking_guests_tablebooking_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebooking',
            name='time',
            field=models.CharField(choices=[('09:00', '9:00 AM'), ('11:00', '11:00 AM')], default='9:00', max_length=5),
        ),
    ]
