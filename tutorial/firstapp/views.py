from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Curriculum

def index1(request) :
    return HttpResponse("<u>Hello World!</u>")

def index2(request) :
    return HttpResponse("<p>index2 함수를 호출했습니다.</p>")

def main(request) :
    return HttpResponse('<u>Main</u>')

def home(request) :
    return HttpResponse('<h1>Home</h1>')

def insert(request) :
    msg = ''
    # 1. create 사용
    Curriculum.objects.create(name='linux')
    msg += '1-linux 입력 성공 <br>'
    # 2. 변수 사용
    c = Curriculum(name='python')
    c.save()
    msg += '2-python 입력 성공 <br>'
    # 3. 바로 save() = commit
    Curriculum(name='3-html/css/js').save()
    msg += '3-html/css/js 입력 성공 <br>'
    Curriculum(name='django').save()
    msg += '4-django 입력 성공'
    return HttpResponse(msg)

def show(request) :
    data = Curriculum.objects.all()
    
    msg = ''
    for dt in data :
        msg += dt.name + '<br>'
        
    return HttpResponse(msg)

def oneshow(request) :
    onedata = Curriculum.objects.get(pk=3)    
    return HttpResponse(onedata.name) 

def update(request) :
    data = Curriculum.objects.get(pk=1)
    data.name = 'linux_update'
    data.save()
    return HttpResponse('데이터 수정완료')

def delete(request) :
    data = Curriculum.objects.get(pk=1)
    data.delete()
    return HttpResponse('데이터 삭제완료')

def show2(request) :
    return render(
        request,
        'firstapp/show2.html',
        {}
    )
    
def show3(request) :
    data = Curriculum.objects.all()
    return render(
        request,
        'firstapp/show3.html',
        {'data' : data}
    )
    
def show4(request) :
    data = Curriculum.objects.all()
    return render(
        request,
        'firstapp/show4.html',
        {'data' : data}
    )