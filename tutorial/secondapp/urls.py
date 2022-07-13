# secondapp.urls
from django.urls import path 
from . import views as sec_v

urlpatterns = [
    path('main/', sec_v.main),
    path('insert/', sec_v.insert),
    path('show/', sec_v.show),
    path('oneshow/', sec_v.oneshow),
    path('show2/', sec_v.show2),
    path('oneshow2/', sec_v.oneshow2),
    path('lprod_list/', sec_v.view_Lprod_List),
    path('lprod/', sec_v.view_Lprod),
]
