# Generated by Django 4.2.16 on 2024-09-16 15:16

from django.conf import settings
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
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('place', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('trip_category', models.CharField(choices=[('LEISURE', 'Leisure'), ('BUSINESS', 'Business'), ('ADVENTURE', 'Adventure'), ('FAMILY', 'Family'), ('ROMANTIC', 'Romantic')], max_length=50)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('trip_status', models.ImageField(choices=[(0, 'Finished'), (1, 'Ongoing'), (2, 'Planned')], default=0, upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='trip.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(blank=True)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='trip.trip')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='trip.trip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)ss', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='trip.trip')),
            ],
        ),
    ]
