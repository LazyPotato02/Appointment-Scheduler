# Generated by Django 5.1.5 on 2025-02-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_remove_appointment_title_appointment_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='phone',
            field=models.CharField(default='', max_length=254),
        ),
    ]
