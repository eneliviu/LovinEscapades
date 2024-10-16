# Generated by Django 4.2.16 on 2024-10-13 17:53

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('place', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)])),
                ('country', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(56)])),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('trip_category', models.CharField(choices=[('Leisure', 'LEISURE'), ('Business', 'BUSINESS'), ('Adventure', 'ADVENTURE'), ('Family', 'FAMILY'), ('Romantic', 'ROMANTIC')], default='LEISURE', max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('trip_status', models.CharField(choices=[('Completed', 'COMPLETED'), ('Ongoing', 'ONGOING'), ('Planned', 'PLANNED')], default='PLANNED')),
                ('shared', models.CharField(choices=[('Yes', 'YES'), ('NO', 'No')], default='YES', max_length=3)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on', 'country', 'start_date'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2)])),
                ('image', cloudinary.models.CloudinaryField(default=None, max_length=255, verbose_name='image')),
                ('description', models.TextField(validators=[django.core.validators.MinLengthValidator(2), django.core.validators.MaxLengthValidator(500)])),
                ('shared', models.BooleanField(default=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trip.trip')),
            ],
            options={
                'ordering': ['-uploaded_at'],
            },
        ),
    ]
