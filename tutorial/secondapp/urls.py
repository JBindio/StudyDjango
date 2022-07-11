# secondapp.urls
from django.urls import path 
from . import views as sec_v

urlpatterns = [
    path('main/', sec_v.main),
    path('insert/', sec_v.insert),
    path('show/', sec_v.show),
    path('oneshow/', sec_v.oneshow),
]
