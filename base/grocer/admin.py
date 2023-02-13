from django.contrib import admin
from .models import *
# Register your models here.

class DishAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'description',
    ]

class MenuAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'from_date',
        'to_date',
        'menu_type',
    ]


class WineAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'producer',
        'wine_type',
        'year',
        'order',
        'is_shown',
        
    ]

    list_filter=[
        'producer',
        'wine_type',
        'is_shown',
        'grapes',
    ]


class ProducerAdmin(admin.ModelAdmin):
    list_display=[
        'name',
        'contact_name',
        'contact_phone',
        'location',
        
    ]
    


admin.site.register(Producer, ProducerAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Ingredient)
#admin.site.register(Allergen)
admin.site.register(Wine, WineAdmin)
admin.site.register(GroceryList)