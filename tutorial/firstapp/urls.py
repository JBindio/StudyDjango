# firstapp.urls
from django.urls import path 
from . import views

urlpatterns = [
    path('main/', views.main),
    path('home/', views.home),
]
