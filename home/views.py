from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import Http404
from bike.models import TwoWheeler
from home.models import UserInfo
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, LoginForm, UserInfoForm, TrialForm
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required


# TEST

class UserInfoView(View):
    form_class = UserInfoForm
    template_name = 'home/userinfo_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = request.user

            info = form.save(commit=False)
            info.user = user
            info.save()
            return redirect('home:index')
        else:
            print(form.errors)

        return render(request, self.template_name, {'form': form})


# Create your views here.
def index(request):
    bike_all = TwoWheeler.objects.filter(verified=True)
    cont = {
        'bike_all': bike_all,
    }
    return render(request, 'home/homepage.html', cont)


class UserFormView(View):
    form_class = UserForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home:index')
        else:
            print("error")
            return render(request, self.template_name, {'form': form})


class UserLogin(View):
    form_class = LoginForm
    template_name = 'home/login.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})


def logout_user(request):

    logout(request)
    return redirect('home:index')


class TrialView(View):
    form_class = TrialForm
    template_name = 'home/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
        else:
            return redirect('bike:index')


@login_required(login_url='/home/login/')
def register(request):
    if request.method == 'POST':
        form = TrialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:index')
        else:
            return redirect('bike:index')
    else:
        form = TrialForm(None)
        return render(request, 'home/trial.html', {'form': form})


@login_required(login_url='/home/login/')
def account_details(request):
    try:
        userinfo = UserInfo.objects.get(user=request.user)
    except UserInfo.DoesNotExist:
        userinfo=None

    if userinfo is not None:
        print(userinfo)
        bike = TwoWheeler.objects.filter(user=request.user)
        args = {
            'userinfo': userinfo,
            'bike': bike,
        }

        return render(request, 'home/det.html', args)
    else:
        return redirect('home:user-info')


def types(request, foo):
    bike_all = TwoWheeler.objects.filter(Model_Type=foo)
    print(foo)
    return render(request, "home/more.html", {'bike_all': bike_all})