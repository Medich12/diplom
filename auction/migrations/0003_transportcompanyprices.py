# Generated by Django 5.0.6 on 2024-06-23 03:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransportCompanyPrices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True)),
                ('id_transport_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.transportcompany')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auction.city')),
            ],
        ),
    ]
