# Generated by Django 5.0.3 on 2024-03-24 21:50

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to=api.models.generate_poster_path),
        ),
    ]
