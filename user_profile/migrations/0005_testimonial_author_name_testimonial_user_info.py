# Generated by Django 4.2.16 on 2024-10-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_testimonial_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='author_name',
            field=models.CharField(default='Anonymous', max_length=50),
        ),
        migrations.AddField(
            model_name='testimonial',
            name='user_info',
            field=models.CharField(default='Enthusiast user', max_length=50),
        ),
    ]
