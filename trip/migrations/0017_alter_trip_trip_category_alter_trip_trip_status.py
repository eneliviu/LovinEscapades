# Generated by Django 4.2.16 on 2024-09-24 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0016_alter_trip_trip_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_category',
            field=models.CharField(choices=[('LEISURE', 'Leisure'), ('BUSINESS', 'Business'), ('ADVENTURE', 'Adventure'), ('FAMILY', 'Family'), ('ROMANTIC', 'Romantic')], default='LEISURE', max_length=50),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_status',
            field=models.IntegerField(choices=[('COMPLETED', 'Completed'), ('ONGOING', 'Ongoing'), ('PLANNED', 'Planned')], default='PLANNED'),
        ),
    ]
