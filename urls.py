from django.urls import path
from . import views

urlpatterns = [path('welcomeapp/', views.members, name='welcomeapp'),]