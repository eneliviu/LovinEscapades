# Generated by Django 4.2.16 on 2024-09-22 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0008_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
