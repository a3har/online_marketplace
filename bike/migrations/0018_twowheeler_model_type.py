# Generated by Django 2.0.5 on 2019-02-16 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0017_auto_20190215_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='twowheeler',
            name='Model_Type',
            field=models.CharField(choices=[('Moped', 'Moped'), ('Bike', 'Bike')], default='Bicycle', max_length=200),
        ),
    ]
