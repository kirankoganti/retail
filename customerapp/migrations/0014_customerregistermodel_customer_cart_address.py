# Generated by Django 4.0.6 on 2022-08-04 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0013_customeraddress_address_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerregistermodel',
            name='customer_cart_address',
            field=models.IntegerField(default=0, help_text='address_id'),
        ),
    ]
