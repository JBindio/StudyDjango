# firstapp.urls
from django.urls import path 
from . import views as front_v

urlpatterns = [
    path('sample_01/', front_v.sample_01),
    path('index_01/', front_v.index_01),
    path('index_css_02/', front_v.index_02),
    path('index_css_03/', front_v.index_03),
    path('index_css_04/', front_v.index_04),
    path('index_css_05/', front_v.index_05),
    path('index_css_06/', front_v.index_06),
    
    
]
