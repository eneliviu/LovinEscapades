# Generated by Django 4.2.16 on 2024-09-30 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0019_alter_trip_trip_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
    ]
