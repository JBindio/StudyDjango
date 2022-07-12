# firstapp.urls
from django.urls import path 
from . import views as fir_v

urlpatterns = [
    path('main/', fir_v.main),
    path('home/', fir_v.home),
    path('insert/', fir_v.insert),
    path('show/', fir_v.show),
    path('oneshow/', fir_v.oneshow),
    path('show2/', fir_v.show2),
    path('show3/', fir_v.show3),
    path('show4/', fir_v.show4),
    path('update/', fir_v.update),
    path('delete/', fir_v.delete),
]
