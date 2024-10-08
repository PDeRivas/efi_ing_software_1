# Generated by Django 5.0.7 on 2024-08-01 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_car_km'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Auto', 'verbose_name_plural': 'Autos'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='fuel',
            options={'verbose_name': 'Combustible', 'verbose_name_plural': 'Combustibles'},
        ),
        migrations.AlterModelOptions(
            name='nameplate',
            options={'verbose_name': 'Modelo', 'verbose_name_plural': 'Modelos'},
        ),
        migrations.AlterModelOptions(
            name='traction',
            options={'verbose_name': 'Tracción', 'verbose_name_plural': 'Tracciones'},
        ),
        migrations.AlterModelOptions(
            name='transmission',
            options={'verbose_name': 'Transmisión', 'verbose_name_plural': 'Transmisiones'},
        ),
    ]
