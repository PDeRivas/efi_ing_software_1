# Generated by Django 5.0.7 on 2024-08-10 17:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_review_time_edit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_number', models.IntegerField()),
                ('city', models.CharField(max_length=100)),
                ('postal_code', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venta', to='cars.car')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pais_comprador', to='cars.country')),
            ],
        ),
    ]
