from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
Cities = (('Pune', 'Pune'), ('Bangalore', 'Bangalore'), ('Mumbai', 'Mumbai'), )


def validate_com(value):
    if 'com' not in value:
        raise ValidationError(_("Invalid Email"))
    return value


# Create your models here.
class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Profile_image = models.ImageField(upload_to='imgas', blank=True)
    name = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=50, choices=Cities)
    state = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=200, default='')
    phone_number = models.CharField(max_length=10, default='')

    def __str__(self):
        return self.name + '  ' + self.state

