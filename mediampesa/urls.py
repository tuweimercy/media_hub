from django.urls import path 
from . import views

app_name = 'mediampesa' #namespace 


urlpatterns = [
    #reveal transaction form
    path('', views.index, name='index'),
    #prompt the stk push function so that user enters pin
    path('stk-push/', views.stk_push, name='stk_push'),
    #for user status update:
    path('waiting/<int:transaction_id>/', views.waiting_page, name='waiting_page'),
    #to reaqd tyhe results of the transaction from mpesa server
    path('callback/', views.callback, name='callback'),
    #update in real time currenty status of transaction
    path('check-status/<int:transaction_id>/', views.check_status, name='check_status'),
    #load the appropriate route according to status
    path('payment-success/',views.payment_success, name='payment_success'),
    path('payment-failed/', views.payment_failed, name='payment_failed'),
    path('payment-cancelled', views.payment_cancelled, name='payment_cancelled'),
]