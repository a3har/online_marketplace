from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

Types = (('Mopeds', 'Mopeds'), ('Bikes', 'Bikes') )

def validate_com(value):
    if 'com' not in value:
        raise ValidationError(_("Invalid Email"))
    return value


# Create your models here.
class TwoWheeler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Model_name = models.CharField(max_length=200, default='')
    Company_name = models.CharField(max_length=100, default='')
    Total_km = models.IntegerField(default=0)
    Description = models.CharField(max_length=1000,  default='')
    Price_before = models.IntegerField(default=0)
    Price_after = models.IntegerField(default=0)
    Mileage = models.IntegerField(default=0)

    Model_img = models.ImageField(upload_to='bike_img', blank=True)
    Left_side = models.ImageField(upload_to='bike_img', blank=True)
    Right_side = models.ImageField(upload_to='bike_img', blank=True)
    Rc_book = models.ImageField(upload_to='bike_img', blank=True)
    Km_Image = models.ImageField(upload_to='bike_img', blank=True)
    Documents_Approved = models.BooleanField(default=False)

    Model_Type = models.CharField(max_length=200, choices=Types, default='Bicycle')

    Suspension = models.CharField(max_length=200, default='-', blank=True)
    Brakes = models.CharField(max_length=200, default='-', blank=True)
    Overall = models.CharField(max_length=200, default='-', blank=True)
    Location = models.CharField(max_length=200, default='-', blank=True)
    verified = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('bike:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.Model_name + '  -  ' + self.Company_name


class TrialTest(models.Model):
    test1 = models.CharField(max_length=50, validators=[validate_com])

    def __str__(self):
        return self.test1
