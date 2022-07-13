# firstapp.urls
from django.urls import path 
from . import views as ora_v

urlpatterns = [
    path('test/', ora_v.test),
    path('oratest/', ora_v.oratest),
    path('member_list/', ora_v.view_Member_list),
    path('member/', ora_v.view_Member),
    path('cart_list/', ora_v.view_Cart_List),
    path('cart_member_list/', ora_v.view_Cart_Member_List),
    path('cart/', ora_v.view_Cart),
    path('cart_insert/', ora_v.set_Cart_Insert),
    path('cart_delete/', ora_v.set_Cart_Delete),
    path('cart_update_form/', ora_v.view_Cart_Update),
    path('testdict/', ora_v.testDict),
    
]
