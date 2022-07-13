from django.http import HttpResponse
from django.shortcuts import render

from .models import Course
from .model_pandas import lprod

# Create your views here.

def main(request) :
    return HttpResponse('<h1><u>Main</u></h1>')

def insert(request) :
    msg = ''
    Course(name='데이터분석', cnt = '30').save()
    msg += '데이터분석 입력완료 <br>'
    Course(name='데이터수집', cnt = '20').save()
    msg += '데이터수집 입력완료 <br>'
    Course(name='웹개발', cnt = '25').save()
    msg += '웹개발 입력완료 <br>'
    Course(name='인공지능', cnt = '20').save()
    msg += '인공지능 입력완료'
    return HttpResponse(msg)


def show(request) :
    msg = ''
    data = Course.objects.all()
    for dt in data :
        msg += dt.name + ' ' + str(dt.cnt) +'<br>'
        
    return HttpResponse(msg)

def oneshow(request) :
    oneshow = Course.objects.get(pk=3)
    msg = oneshow.name + ' ' + str(oneshow.cnt)    
    return HttpResponse(msg)

def show2(request) :
    data = Course.objects.all()
    return render(
        request,
        'secondapp/show2.html',
        {'data' : data}
    )
    
def oneshow2(request) :
    data = Course.objects.get(pk=4)
    return render(
        request,
        'secondapp/oneshow2.html',
        {'data' : data}
    )
    
def view_Lprod_List(request) :
    
    df = lprod.getLprodList()
    context = {'df' : df}
    return render(
        request,
        'secondapp/lprod/lprod_list.html',
        context
    )
    
def view_Lprod(request) :
    
    lprod_gu = request.GET['lprod_gu']
    
    df = lprod.getLprod(lprod_gu)
    
    return render(
        request,
        'secondapp/lprod/lprod.html',
        df
    )