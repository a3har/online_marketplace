from django.urls import include,path
from . import views

app_name = 'bike'

#
urlpatterns = [
    path('', views.bike, name='index'),

    #/bike/2/
    path('(?P<pk>[0-9]+)/', views.details, name='details'),

    #/bike/add/
    path('add/', views.BikeInsertView.as_view(), name='bike-add'),

    path('yourbikes/',views.uploaded,name='bike-upload'),

    path('trial/', views.TrialView.as_view(), name='trial'),
]
