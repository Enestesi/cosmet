from django.db import models
from users.models import User
from services.models import Basket


class Order(models.Model):
    CREATED = 0
    CONFIRMED = 1
    VIZITED = 2
    CANCEL = 3
    STATUSES = (
        (CREATED,'На подтверждении'),
        (CONFIRMED, 'Подтверждена'),
        (VIZITED,'Посетил'),
        (CANCEL,'Отменена'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    date = models.DateField()
    time = models.TimeField()
    basket_history = models.JSONField(default=dict)
    created = models.DateField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Запись №{self.id}. {self.first_name} {self.last_name} на {self.date.strftime("%d-%m-%Y")} в {self.time.strftime("%H:%M")}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def after_create(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.basket_history = {
            'orders_items': [basket.de_json() for basket in baskets],
            'total_sum': float(baskets.total_sum()),
        }
        baskets.delete()
        self.save()
















