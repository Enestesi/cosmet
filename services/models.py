from django.db import models

from users.models import User


class CategoryServices(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Services(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    time = models.CharField(max_length=20)
    image = models.ImageField(upload_to='services_images')
    category = models.ForeignKey(to=CategoryServices, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return f'Услуга: {self.name}| Категория: {self.category.name}'


class BasketQuerySet(models.QuerySet):
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    services = models.ForeignKey(to=Services, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт: {self.services.name}'

    def sum(self):
        return self.services.price * self.quantity

    def de_json(self):
        basket_item = {
            'service_name': self.services.name,
            'quantity': self.quantity,
            'price': float(self.services.price),
            'sum': float(self.sum())
        }
        return basket_item



class PhotoDoPosle(models.Model):
    name = models.CharField(max_length=128, unique=False)
    image = models.ImageField(upload_to='do_posle_images')


