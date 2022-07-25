from tracemalloc import start
from django.http import HttpResponse
from django.shortcuts import render

# 생성한 모델 임포트
from .model_pandas import member as mem
from .model_pandas import cart
from .model_pandas import login

# 페이징처리 라이브러리
from django.core.paginator import Paginator

# ----------------------------------------------------------------------------------------------------------

def test(request) :
    return HttpResponse('오라클App 테스트')

# ----------------------------------------------------------------------------------------------------------

def oratest(request) :
    return render(
        request,
        'oracleapp/oratest.html',
        {}
    )

# ----------------------------------------------------------------------------------------------------------
    
# 회원 전체 조회하기
def view_Member_List(request) :
    
    df = mem.getMemberList()
    context = {'df' : df}
    
    return render(
        request,
        'oracleapp/member/member_list.html',
        context
    )

# ----------------------------------------------------------------------------------------------------------   

# 주문내역 전체 조회 페이징 처리
def view_Member_List_Page(request) :
    
    # 페이징 처리1 시작
    try :
        now_page = request.GET.get('page')
        now_page = int(now_page)
    
    except :
        now_page = 1
    # 페이징 처리1 끝
    
    # 모델 조회
    df = mem.getMemberList()
    
    # 페이징 처리2 시작
    
    # 라이브러리 추가 from django.core.paginator import Paginator
    # Paginator(조회모델, 나눌페이지수)
    p = Paginator(df, 5)

    # 페이지 추출
    info = p.get_page(now_page)
    
    # 시작 페이지 
    start_page = (now_page - 1) // 3 * 3 + 1
    # 마지막 페이지
    end_page = start_page + 2
    
    # p.num_pages : 전체 페이지 수
    # end_page : 계산에 의한 페이지 수 (10 단위 계산)
    # 전체 페이지 수보다 큰 경우 처리
    if end_page > p.num_pages :
        end_page = p.num_pages
    
    # 이전 페이지 가기
    is_prev = False
    # 다음 페이지 가기
    is_next = False
    
    # 이전/ 다음 체크하기
    if start_page > 1:
        is_prev = True
    
    if end_page < p.num_pages:
        is_next = True
    
    # 페이징 처리2 끝
    context = {'info'        : info,
                'page_range' : range(start_page, end_page +1),
                'is_prev'    : is_prev,
                'is_next'    : is_next,
                'start_page' : start_page,
                'end_page'   : end_page}
    return render(
        request,
        'oracleapp/page_control/member_list_page.html',
        context
    )

# ----------------------------------------------------------------------------------------------------------    
    
# 회원 상세조회하기
def view_Member(request) :
    
    mem_id = request.GET['mem_id']
    df_dict = mem.getMember(mem_id)
    
    return render(
        request,
        'oracleapp/member/member.html',
        df_dict
    )
    
# ----------------------------------------------------------------------------------------------------------
    
def view_Cart_List(request) :
    
    df = cart.getCartList()
    context = {'df' : df}
    return render(
        request,
        'oracleapp/cart/cart_list.html',
        context
    )

# ----------------------------------------------------------------------------------------------------------    
    
def view_Cart_Member_List(request) :
    
    df = cart.getCartMemberList('a001')
    context = {'df' : df}
    return render(
        request,
        'oracleapp/cart/cart_member_list.html',
        context
    )

# ----------------------------------------------------------------------------------------------------------

def view_Cart(request) :
    
    pcart_no = request.GET['pcart_no']
    pcart_prod = request.GET['pcart_prod']
    df_dict = cart.getCart(pcart_no, pcart_prod)
    
    return render(
        request,
        'oracleapp/cart/cart.html',
        df_dict
    )
# ----------------------------------------------------------------------------------------------------------
    
def set_Cart_Insert(request) :
    pcart_member = request.POST['pcart_member']
    pcart_prod = request.POST['pcart_prod']
    cart_qty = request.POST['cart_qty']
    
    msg = cart.setCartInsert(pcart_member,pcart_prod,cart_qty)
    
    if msg =='Y' :
        pageControl = '''<script>
                            alert('입력이 완료되었습니다.')
                            location.href='/oracle/cart_list/'
                         </script>
                      '''
    else :
        pageControl = '''<script>
                            alert('입력에 실패했습니다. 다시 시도하세요')
                            history.go(-1)
                         </script>
                      '''
    return HttpResponse(pageControl)

# ----------------------------------------------------------------------------------------------------------

def view_Cart_Insert(request) :
    
    pcart_member = 'e001'
    pcart_prod = 'P102000001'
    
    return render(
        request,
        'oracleapp/cart/cart_insert_form.html',
        {'pcart_member':pcart_member, 'pcart_prod':pcart_prod}
    )

# ----------------------------------------------------------------------------------------------------------

def set_Cart_Delete(request) :
    pcart_no = request.GET['pcart_no']
    pcart_prod = request.GET['pcart_prod']
    
    msg = cart.setCartDelete(pcart_no, pcart_prod)
    
    if msg =='Y' :
        pageControl = '''<script>
                            alert('삭제가 완료되었습니다.')
                            location.href='/oracle/cart_list/'
                         </script>
                      '''
    else :
        pageControl = '''<script>
                            alert('삭제에 실패했습니다. 다시 시도하세요')
                            history.go(-1)
                         </script>
                      '''
    return HttpResponse(pageControl)

# ----------------------------------------------------------------------------------------------------------
    
def view_Cart_Update(request) :
    pcart_no = request.GET['pcart_no']
    pcart_prod = request.GET['pcart_prod']
    
    df_dict = cart.getCart(pcart_no, pcart_prod)
    df_dict['pcart_no'] = pcart_no
    df_dict['pcart_prod'] = pcart_prod
    
    # context = {'pcart_no': pcart_no, 
    #            'pcart_prod' : pcart_prod}
    
    return render(
        request,
        'oracleapp/cart/cart_update_form.html',
        df_dict
    )

# ----------------------------------------------------------------------------------------------------------

def set_Cart_Update(request) :
    pcart_no = request.POST['pcart_no']
    pcart_prod = request.POST['pcart_prod']
    cart_qty = request.POST['cart_qty']
    
    msg = cart.setCartUpdate(pcart_no, pcart_prod, cart_qty)
    
    if msg =='Y' :
        pageControl = '''<script>
                            alert('수정이 완료되었습니다.')
                            location.href='/oracle/cart_list/'
                         </script>
                      '''
    else :
        pageControl = '''<script>
                            alert('수정에 실패했습니다. 다시 시도하세요')
                            history.go(-1)
                         </script>
                      '''
    return HttpResponse(pageControl)
    # return render(
    #     request,
    #     'oracleapp/cart/cart_update.html',
    #     {'msg': msg}
    # )

# ----------------------------------------------------------------------------------------------------------

# 주문내역 전체 조회 페이징 처리
def view_Cart_List_Page(request) :
    
    # 페이징 처리1 시작
    try :
        now_page = request.GET.get('page')
        now_page = int(now_page)
    
    except :
        now_page = 1
    # 페이징 처리1 끝
    
    # 모델 조회
    df = cart.getCartList()
    
    # 페이징 처리2 시작
    
    # 라이브러리 추가 from django.core.paginator import Paginator
    # Paginator(조회모델, 나눌페이지수)
    p = Paginator(df, 10)

    # 페이지 추출
    info = p.get_page(now_page)
    
    # 시작 페이지 
    start_page = (now_page - 1) // 10 * 10 + 1
    # 마지막 페이지
    end_page = start_page + 9
    
    # p.num_pages : 전체 페이지 수
    # end_page : 계산에 의한 페이지 수 (10 단위 계산)
    # 전체 페이지 수보다 큰 경우 처리
    if end_page > p.num_pages :
        end_page = p.num_pages
    
    # 이전 페이지 가기
    is_prev = False
    # 다음 페이지 가기
    is_next = False
    
    # 이전/ 다음 체크하기
    if start_page > 1:
        is_prev = True
    
    if end_page < p.num_pages:
        is_next = True
    
    # 페이징 처리2 끝
    context = {'info'        : info,
                'page_range' : range(start_page, end_page +1),
                'is_prev'    : is_prev,
                'is_next'    : is_next,
                'start_page' : start_page,
                'end_page'   : end_page}
    return render(
        request,
        'oracleapp/page_control/cart_list_page.html',
        context
    )

# ----------------------------------------------------------------------------------------------------------

# 로그인 화면
def view_Login_Form(request):
    return render(
        request,
        'oracleapp/login/login_form.html',
        {}
    )

# ----------------------------------------------------------------------------------------------------------

# 로그인 정보 화면   
def get_Login(request):
    pmem_id = request.POST['mem_id']
    pmem_pass = request.POST['mem_pass']
    
    df_dict = login.getLogin(pmem_id, pmem_pass)
    # 로그인 실패 시 처리
    if df_dict['rs'] == 'no':
        context = '''<script>
                        alert('로그인 실패. 아이디 또는 패스워드를 확인하세요.')
                        history.go(-1)
                    </script>'''
        return HttpResponse(context)
    
    df_dict['pmem_id'] = pmem_id
    df_dict['pmem_pass'] = pmem_pass

    # Session 처리 (회원 정보를 서버에 저장해 놓고 있는 상태)
    # (로그아웃 하기전 까지 회원 정보 유지)
    # request.session[]
    # session에 저장되는 값 = 딕셔너리 형태
    # session 등록하기
    request.session['sMem_id'] = pmem_id
    request.session['sMem_name'] = df_dict['mem_name']
    
    # Session에 저장된 값 불러오기
    if request.session.get('sMem_id') :
        # 세션에 값이 있는경우
        df_dict['sMem_id'] = request.session['sMem_id']
        df_dict['sMem_name'] = request.session['sMem_name']
    else:
        # 세션에 값이 없는경우
        df_dict['sMem_id'] = None

    return render(
        request,
        # 'oracleapp/login/login.html',
        'oracleapp/login/login_form.html',
        df_dict
    )

# ----------------------------------------------------------------------------------------------------------

# 로그아웃  
def set_Logout(request) :
    if request.session.get('sMem_id') :
        # 세션정보 삭제하기
        request.session.flush()
        
        context = '''<script>
                        alert('로그아웃 되었습니다')
                        location.href='/oracle/login_form/'
                     </script>'''
        return HttpResponse(context)

    else : 
        context = '''<script>
                        alert('직접 접근할 수 없습니다, 로그인 페이지로 이동합니다')
                        location.href='/oracle/login_form/'
                     </script>'''
        return HttpResponse(context)    
    
# ----------------------------------------------------------------------------------------------------------   

# Dict 변환 테스트    
def testDict(request) :
    context = {'context' : [{'no1':1,'no2':2,'no3':3},
                            {'no1':4,'no2':5,'no3':6}]}
    return render(
        request,
        'oracleapp/test_dict.html',
        context
    )
