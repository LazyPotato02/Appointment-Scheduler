# Generated by Django 5.1.5 on 2025-02-02 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_appointer',
            field=models.BooleanField(default=False),
        ),
    ]
