# Generated by Django 5.1.4 on 2025-01-16 21:41

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('skillflow', '0004_weeklyschedule_schedule_type_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='weeklyschedule',
            unique_together={('provider', 'service', 'day_of_week', 'start_time')},
        ),
        migrations.RemoveField(
            model_name='weeklyschedule',
            name='schedule_type',
        ),
        migrations.RemoveField(
            model_name='weeklyschedule',
            name='specific_date',
        ),
    ]
