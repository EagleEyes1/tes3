# Generated by Django 4.0.5 on 2022-06-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jenisikan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenisikan',
            name='g_ikan',
            field=models.CharField(max_length=999999999),
        ),
    ]
