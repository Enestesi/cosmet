
from .models import Order
from services.models import Basket
from django.shortcuts import render
from datetime import datetime



def first_page(request):
    all_time = ['08:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']

    yesterday = datetime.today()
    min_day_value = yesterday.strftime("%Y-%m-%d")

    if request.GET.get('date') is None:
        context = {
            'min_day_value': min_day_value,
            'all_time': all_time,
            'baskets': Basket.objects.filter(user=request.user),
            'step_1': True,
            'step': 'Шаг 1'
        }
        return render(request, 'procedures/order-create.html', context)
    else:
        appointments = Order.objects.filter(date=request.GET.get('date')).all()
        for obj in appointments:
            if obj.time.strftime("%H:%M") in all_time:
                all_time.remove(obj.time.strftime("%H:%M"))
        context = {
            'min_day_value': min_day_value,
            'all_time': all_time,
            'baskets': Basket.objects.filter(user=request.user),
            'step_1': False,
            'step_2': True,
            'step': 'Шаг 2',
            'selected_date': request.GET.get('date')
        }
        return render(request, 'procedures/order-create.html', context)


def appointment(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        selected_date = request.POST['date']
        time = request.POST['time']
        initiator = request.user

        element = Order(first_name=first_name, last_name=last_name, date=selected_date, time=time, initiator=initiator)
        element.save()
        element.after_create()
        return render(request, 'procedures/success.html', {'name': first_name, })
    else:
        return render(request, 'procedures/success.html')


def OrderList(request):
    all_orders = Order.objects.all()
    orders = all_orders.filter(initiator=request.user).order_by('-id')
    context = {
        'title': 'Записи',
        'orders': orders,
    }
    return render(request, 'procedures/orders.html', context)


def OrderDetail(request, order_id):
    order = Order.objects.get(id=order_id)
    services = order.basket_history
    context = {
        'title': 'Записи',
        'services': services,
        'id': order_id,
    }
    return render(request, 'procedures/order.html', context)
