# Generated by Django 3.2.16 on 2022-11-21 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qna',
            name='region',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='qna',
            name='place',
            field=models.CharField(max_length=30),
        ),
    ]
