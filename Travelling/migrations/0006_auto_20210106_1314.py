# Generated by Django 3.1.3 on 2021-01-06 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Travelling', '0005_passengerdata_tcost'),
    ]

    operations = [
        migrations.AddField(
            model_name='passengerdata',
            name='destnation',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='passengerdata',
            name='sorce',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
