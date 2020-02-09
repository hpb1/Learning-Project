from django.shortcuts import render
from . import views

app_name = 'main'
urlpatterns = [
    path('',views.homepage,name='homepage'),
]