from django.contrib import admin

# Register your models here.
from services.models import CategoryServices, Services, Basket, PhotoDoPosle


admin.site.register(CategoryServices)
admin.site.register(PhotoDoPosle)

@admin.register(Services)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'time', 'category')
    search_fields = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('services', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0