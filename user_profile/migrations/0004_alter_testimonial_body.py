# Generated by Django 4.2.16 on 2024-09-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_testimonial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
