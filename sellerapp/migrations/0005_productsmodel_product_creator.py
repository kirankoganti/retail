# Generated by Django 4.0.6 on 2022-07-28 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0004_productsmodel_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='product_creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sellerapp.sellerregistermodel'),
        ),
    ]
