# Generated by Django 4.0.5 on 2022-06-29 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('barmas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmasuk',
            name='harga',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bmasuk',
            name='ket',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='bmasuk',
            name='b_gambar',
            field=models.CharField(max_length=999999999),
        ),
    ]
