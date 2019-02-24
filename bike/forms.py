from django.contrib.auth.models import User
from .models import TwoWheeler, TrialTest
from django import forms
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class BikeInsertForm(forms.ModelForm):
    class Meta:
        model = TwoWheeler
        widgets = {
            'Description': forms.Textarea(attrs={'rows': 4}),
        }
        exclude = ['user', 'verified', 'Suspension', 'Brakes', 'Overall', 'Location', 'Mileage']
        fields = [
            'Model_name',
            'Company_name',
            'Total_km',
            'Description',
            'Model_img',
            'Left_side',
            'Left_side',
            'Km_Image',
            'Right_side',
            'Rc_book',
            'Price_before',
            'Price_after',
        ]


class TrialForm(forms.ModelForm):
    class Meta:
        model = TrialTest
        fields = ['test1']
