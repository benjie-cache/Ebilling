# Generated by Django 4.0.3 on 2022-12-05 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_client_secondary_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='managerclientcommunication',
            old_name='body',
            new_name='message',
        ),
        migrations.RemoveField(
            model_name='managerclientcommunication',
            name='subject',
        ),
    ]
