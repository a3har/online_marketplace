from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from bike.models import TwoWheeler, TrialTest
from bike.forms import BikeInsertForm, TrialForm
from django.views.generic import View
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.decorators import login_required


# Create your views here.
def bike(request):
    bike_all = TwoWheeler.objects.all()
    con = {
        'bike_all': bike_all,
    }
    return render(request, "bike/first.html", con)


def details(request, pk):
    try:
        x = TwoWheeler.objects.get(pk=pk)
    except TwoWheeler.DoesNotExist:
        raise Http404("Vehicle Not Found")
    con = {
        'bikes': x,
    }
    return render(request, 'home/bikedet.html', con)


class BikeInsertView(View):
    form_class = BikeInsertForm
    template_name = 'bike/vehiclereg.html'

    def get(self, request):
        user = request.user
        if user.is_authenticated:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('home:login')
        

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            user = request.user

            bike1 = form.save(commit=False)
            bike1.user = user
            bike1.save()
            return redirect('home:index')
        else:
            print(form.errors)
            return render(request, self.template_name, {'form': form})


class TrialView(View):
    form_class = TrialForm
    template_name = 'bike/trial.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home:index')

        return render(request, self.template_name, {'form': form})


def uploaded(request):
    user = request.user
    if user.is_authenticated:
        bike_all = TwoWheeler.objects.filter(user=user)
        return render(request, "bike/regstatus.html", {'bike_all': bike_all})
    else:
        return redirect('home:login')


