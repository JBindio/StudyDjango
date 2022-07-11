from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index1(request):
    return HttpResponse('<h1>안녕하세요 오늘은 비가 옵니다</h1>')