# Generated by Django 4.0.5 on 2022-07-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barmas', '0002_bmasuk_harga_bmasuk_ket_alter_bmasuk_b_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmasuk',
            name='k_ikan',
            field=models.DecimalField(decimal_places=5, max_digits=99),
        ),
    ]
