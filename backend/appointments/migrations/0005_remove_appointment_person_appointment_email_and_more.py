# Generated by Django 5.1.5 on 2025-02-09 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_appointment_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='person',
        ),
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.EmailField(default='unknown@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='appointment',
            name='first_name',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AddField(
            model_name='appointment',
            name='last_name',
            field=models.CharField(default='Person', max_length=100),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='phone',
            field=models.CharField(default='0000000000', max_length=20),
        ),
    ]
