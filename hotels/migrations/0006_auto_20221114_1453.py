# Generated by Django 3.2.13 on 2022-11-14 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0005_alter_hotel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='hotelreview',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
