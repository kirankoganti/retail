# Generated by Django 4.0.6 on 2022-08-05 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0015_alter_ordersmodels_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordersmodels',
            name='order_payment_id',
            field=models.CharField(help_text='Payment_id_from_razorpay', max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='OrderProductsModels',
        ),
    ]
