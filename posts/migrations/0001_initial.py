# Generated by Django 4.1.4 on 2023-01-04 18:43

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='Anonymous', max_length=16, verbose_name='Name')),
                ('body', models.CharField(db_index=True, default='Type the text', max_length=140, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DateTime')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image')),
                ('likes', models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Likes')),
            ],
            options={
                'db_table': 'post',
            },
        ),
    ]