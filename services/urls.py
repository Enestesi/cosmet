from django.urls import path
from services.views import services, basket_add, basket_remove, stock, photo
app_name = 'services'

urlpatterns = [
    path('', services, name='index'),
    path('category/<int:category_id>', services, name='category'),
    path('page/<int:page_number>', services, name='paginator'),
    path('baskets/add/<int:service_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('stock/', stock, name='stock'),
    path('photo/', photo, name='photo'),
]