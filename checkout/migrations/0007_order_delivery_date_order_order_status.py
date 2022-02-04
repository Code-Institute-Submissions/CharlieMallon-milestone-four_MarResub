# Generated by Django 4.0.1 on 2022-02-04 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]