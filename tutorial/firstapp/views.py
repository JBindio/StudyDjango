from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index1(request) :
    return HttpResponse("<u>Hello World!</u>")

def index2(request) :
    return HttpResponse("<p>index2 함수를 호출했습니다.</p>")

def main(request) :
    return HttpResponse('<u>Main</u>')

def home(request) :
    return HttpResponse('<h1>Home</h1>')