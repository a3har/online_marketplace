# Generated by Django 2.0.5 on 2019-02-16 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0018_twowheeler_model_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twowheeler',
            name='Model_Type',
            field=models.CharField(choices=[('Mopeds', 'Mopeds'), ('Bikes', 'Bikes')], default='Bicycle', max_length=200),
        ),
    ]
