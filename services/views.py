from django.shortcuts import render, HttpResponseRedirect
from services.models import CategoryServices, Services, Basket, PhotoDoPosle
from django.contrib.auth.decorators import login_required
from users.models import User
from django.core.paginator import Paginator

def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'services/index.html', context)

    # if category_id:
    #     services = Services.objects.filter(category_id=category_id)
    # else:
    #     services = Services.objects.all()


def services(request, category_id=None, page_number=1):

    services = Services.objects.filter(category_id=category_id) if category_id else Services.objects.all()

    per_page = 6
    paginator = Paginator(services, per_page)
    services_paginator = paginator.page(page_number)

    context = {
        'title': 'Каталог',
        'services': services_paginator,
        'categories': CategoryServices.objects.all(),
    }
    return render(request, 'services/services.html', context)


@login_required
def basket_add(request, service_id):
    services = Services.objects.get(id=service_id)
    baskets = Basket.objects.filter(user=request.user, services=services)

    if not baskets.exists():
        Basket.objects.create(user=request.user, services=services, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def stock(request):
    context = {
        'title': 'Акции',
    }
    return render(request, 'services/stock.html', context)


def photo(request):
    context = {
        'title': 'Фотографии',
        'PhotoDoPosle': PhotoDoPosle.objects.all(),
    }
    return render(request, 'services/Photo.html', context)



