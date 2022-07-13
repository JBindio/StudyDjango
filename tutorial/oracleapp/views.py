from importlib.resources import contents
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
    
    mem_id = request.GET['mem_id']
    df_dict = mem.getMember(mem_id)
    
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
    
    cart_no = request.GET['cart_no']
    cart_prod = request.GET['cart_prod']
    df_dict = cart.getCart(cart_no, cart_prod)
    
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

def set_Cart_Delete(request) :
    cart_no = request.GET['cart_no']
    cart_prod = request.GET['cart_prod']
    
    msg = cart.setCartDelete(cart_no, cart_prod)
    
    return render(
        request,
        'oracleapp/cart/cart_delete.html',
        {'msg':msg}
    )
    
def view_Cart_Update(request) :
    pcart_no = request.GET['cart_no']
    pcart_prod = request.GET['cart_prod']
    
    # msg = cart.setCartDelete(cart_no, cart_prod)
    
    context = {'pcart_no': pcart_no, 
               'pcart_prod' : pcart_prod}
    
    return render(
        request,
        'oracleapp/cart/cart_update_form.html',
        context
    )

def testDict(request) :
    context = {'context' : [{'no1':1,'no2':2,'no3':3},
                            {'no1':4,'no2':5,'no3':6}]}
    return render(
        request,
        'oracleapp/test_dict.html',
        context
    )
    
