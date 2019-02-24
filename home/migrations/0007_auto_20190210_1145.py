# Generated by Django 2.1.2 on 2019-02-10 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190209_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='Profile_image',
            field=models.ImageField(default='home/assets/default_img.jpg', upload_to='profile_pic'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
    ]
