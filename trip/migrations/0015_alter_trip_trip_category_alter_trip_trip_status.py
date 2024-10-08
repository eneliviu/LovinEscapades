# Generated by Django 4.2.16 on 2024-09-24 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0014_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='trip_category',
            field=models.CharField(choices=[('Leisure', 'Leisure'), ('Business', 'Business'), ('Adventure', 'Adventure'), ('Family', 'Family'), ('Romantic', 'ROMANTIC')], max_length=50),
        ),
        migrations.AlterField(
            model_name='trip',
            name='trip_status',
            field=models.IntegerField(choices=[('Completed', 'Completed'), ('Ongoing', 'Ongoing'), ('Planned', 'Planned')], default=0),
        ),
    ]
