# Generated by Django 2.0.5 on 2019-02-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0015_auto_20190210_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='twowheeler',
            name='Brakes',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='twowheeler',
            name='Location',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='twowheeler',
            name='Mileage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='twowheeler',
            name='Overall',
            field=models.CharField(default='-', max_length=200),
        ),
        migrations.AddField(
            model_name='twowheeler',
            name='Suspension',
            field=models.CharField(default='-', max_length=200),
        ),
    ]