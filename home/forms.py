from django.contrib.auth.models import User
from .models import UserInfo
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def validate_user(value):
    if User.objects.filter(username=value).exists():
        raise ValidationError(_("Email Already exits"))
    return value


class UserForm(forms.ModelForm):
    username = forms.CharField(validators=[validate_user])
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        print(username)
        if username and password:
            user1 = User.objects.filter(username=username)
            print(user1.username)
            if user1.password != password:
                raise ValidationError(_("Password!!"))


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        exclude = ['user']
        fields = ['name', 'Profile_image', 'city', 'state', 'address', 'phone_number']


class TrialForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2', 'email']

    def save(self, commit=True):
        user = super(TrialForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user


