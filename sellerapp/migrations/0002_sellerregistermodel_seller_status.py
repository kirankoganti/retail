# Generated by Django 4.0.6 on 2022-07-27 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellerregistermodel',
            name='seller_status',
            field=models.CharField(default='Pending', help_text='seller_status', max_length=15),
        ),
    ]