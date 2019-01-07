from django.urls import path
from . import views
from django.views.generic import TemplateView
from apps.account.views import create_account, account_index, account_close, \
account_tarea, account_grupo, account_add_to_group, account_ver
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('inicio/', account_index, name='inicio'),
    path('registro/', create_account, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', account_close, name='logout'),
    path('tarea/', account_tarea, name='tarea'),
    path('grupo/', account_grupo, name='grupo'),
    path('add/', account_add_to_group, name='add_to_grupo'),
    path('ver/', account_ver, name='ver'),
]