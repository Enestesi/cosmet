from django.urls import path
from procedures.views import first_page, appointment, OrderList, OrderDetail
app_name = 'procedures'

urlpatterns = [
    path('thanks/',appointment, name='appointment'),
    path('order-create/', first_page, name='first_page'),
    path('', OrderList , name='orders_list'),
    path('order/<int:order_id>', OrderDetail, name='order')
]