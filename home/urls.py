from django.urls import include,path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),

    path('register/', views.UserFormView.as_view(), name='register'),

    path('login/', views.UserLogin.as_view(), name='login'),

    path('logout/', views.logout_user, name='user-logout'),

    path('account/', views.account_details, name='acc-details'),

    path('userinfo/', views.UserInfoView.as_view(), name='user-info'),

    path('trial/', views.register, name='trial'),

    path('types/bikes/<slug:foo>', views.types, name='types'),
]
