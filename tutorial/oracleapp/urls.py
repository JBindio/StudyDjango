# firstapp.urls
from django.urls import path 
from . import views as ora_v
app_name = 'oracle'

urlpatterns = [
    path('test/', ora_v.test),
    path('oratest/', ora_v.oratest),
    path('member_list/', ora_v.view_Member_List),
    path('member_list_page/', ora_v.view_Member_List_Page, name='member_list_page'),
    path('member/', ora_v.view_Member),
    path('cart_list/', ora_v.view_Cart_List),
    path('cart_member_list/', ora_v.view_Cart_Member_List),
    path('cart/', ora_v.view_Cart),
    path('cart_insert_form/', ora_v.view_Cart_Insert),
    path('cart_insert/', ora_v.set_Cart_Insert),
    path('cart_delete/', ora_v.set_Cart_Delete),
    path('cart_update_form/', ora_v.view_Cart_Update),
    path('cart_update/', ora_v.set_Cart_Update),   
    path('cart_list_page/', ora_v.view_Cart_List_Page, name='cart_list_page'),
    path('testdict/', ora_v.testDict),
    path('login_form/', ora_v.view_Login_Form),
    path('login/', ora_v.get_Login),
    path('logout/', ora_v.set_Logout),
    
]
