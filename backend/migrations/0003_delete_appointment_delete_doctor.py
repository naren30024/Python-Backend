# Generated by Django 4.1.7 on 2023-10-05 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_registration'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Appointment',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]