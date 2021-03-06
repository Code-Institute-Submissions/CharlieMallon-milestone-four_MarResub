# Generated by Django 4.0.1 on 2022-01-25 15:59

from django.db import migrations, models
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='county',
            field=django_countries.fields.CountryField(default='UK', max_length=2),
        ),
    ]
