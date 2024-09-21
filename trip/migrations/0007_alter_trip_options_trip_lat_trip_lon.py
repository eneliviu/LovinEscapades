# Generated by Django 4.2.16 on 2024-09-21 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0006_trip_shared'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trip',
            options={'ordering': ['-created_on', 'start_date', 'country']},
        ),
        migrations.AddField(
            model_name='trip',
            name='lat',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='trip',
            name='lon',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
