# Generated by Django 4.2.16 on 2024-10-06 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0025_alter_image_description_alter_image_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='shared',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='trip',
            name='shared',
            field=models.CharField(choices=[('Yes', 'YES'), ('NO', 'No')], default='YES', max_length=3),
        ),
    ]
