# Generated by Django 4.0.3 on 2022-11-27 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_waterconsumption_consumption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='waterbillingcycle',
            name='units',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
