from django.urls import path
from . import views
from django.conf.urls import  url, include

urlpatterns = [
    path('screens/', views.screens, name='screens'),
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    url('select-square', views.selectSquare, name='select-square')
]
