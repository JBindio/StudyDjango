from django.http import HttpResponse
from django.shortcuts import render
from .model_pandas import member as mem
from .model_pandas import cart

# Create your views here.

def test(request) :
    return HttpResponse('오라클App 테스트')

def oratest(request) :
    return render(
        request,
        'oracleapp/oratest.html',
        {}
    )
    
# 회원 전체 조회하기
def view_Member_list(request) :
    
    df = mem.getMemberList()
    context = {'df' : df}
    
    return render(
        request,
        'oracleapp/member/member_list.html',
        context
    )
# 회원 상세조회하기
def view_Member(request) :
    
    df_dict = mem.getMember('a001')
    # context = {'df' : df}
    
    return render(
        request,
        'oracleapp/member/member.html',
        df_dict
    )
    
def view_Cart_List(request) :
    
    df = cart.getCartList()
    context = {'df' : df}
    return render(
        request,
        'oracleapp/cart/cart_list.html',
        context
    )
    
def view_Cart_Member_List(request) :
    
    df = cart.getCartMemberList('a001')
    context = {'df' : df}
    return render(
        request,
        'oracleapp/cart/cart_member_list.html',
        context
    )

def view_Cart(request) :
    
    df_dict = cart.getCart('2005040100001','P302000003')
    return render(
        request,
        'oracleapp/cart/cart.html',
        df_dict
    )
    
def set_Cart_Insert(request) :
    id = 'e001'
    prod = 'P102000001'
    qty = 17
    
    msg = cart.setCartInsert(id,prod,qty)
    
    return HttpResponse(msg)