# Generated by Django 3.0 on 2020-05-20 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Flight', '0004_bookings_flight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookings',
            name='flight',
        ),
        migrations.AddField(
            model_name='bookings',
            name='route',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bookedflight', to='Flight.Flight'),
        ),
    ]
