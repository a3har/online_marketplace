# Generated by Django 2.0.5 on 2019-02-15 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_userinfo_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Profile_image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]