from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings
#from django.contrib import admin

from . import views
from django.contrib.auth import views as auth_views

#VISTAS
#from Login.views import Index

from Login.views import LoginClass
from Landing.views import LandingClass
from Dashboard.views import DashboardClass
#from Login.views import Landing
#URL QUE MANEJAN LOS PARAMETROS DASHBOARD
app_name = 'Login'

urlpatterns = [

    path('',LoginClass.as_view(), name = 'login'),
    # path('Dashboard',DashboardClass.as_view(), name = 'Dashboard')
    
    # path ('',LandingClass.as_view(),name='landing'),
    # path ('login',LoginClass.as_view(),name='login'),
    # path ('landing',LandingClass.as_view(),name='landing'),
    # path ('dashboard',DashboardClass.as_view(),name='dashboard'),

    #path('', views.Landing,name='Landing'),
    #path('', LoginClass.as_view(), name='Login'),
    #path('login/', views.Index,name='Index'),
]