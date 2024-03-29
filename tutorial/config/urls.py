"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 

from firstapp import views as fir_v
from secondapp import views as sec_v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1/', fir_v.index1),
    path('index2/', fir_v.index2),
    path('first/', include('firstapp.urls')),
    path('second/', include('secondapp.urls')),
    path('oracle/', include('oracleapp.urls')),
    path('frontend/', include('frontendapp.urls')),
    path('chi2/', include('chi2app.urls')),
    # path('home/', views.home),
]
