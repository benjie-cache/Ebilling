# Generated by Django 4.1.3 on 2022-12-03 05:52

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_waterbillingcycle_due_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='secondary_phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None),
        ),
    ]
