# Generated by Django 5.1.5 on 2025-02-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_appointment_is_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='title',
        ),
        migrations.AddField(
            model_name='appointment',
            name='person',
            field=models.CharField(default='', max_length=254),
        ),
    ]
