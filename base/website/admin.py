from django.contrib import admin
from .models import *

class Gallery_imageAdmin(admin.ModelAdmin):
    list_display=('header', 'description', 'is_first', 'show_image')


class DishAdmin(admin.ModelAdmin):
    list_display=('name', 'price', 'description', 'type')
    search_fields=("name", 'price')
    list_filter=('type',)


class MenuAdmin(admin.ModelAdmin):
    list_display=('id','is_lunch','pub_date')
    list_filter=("is_lunch",)


class WineAdmin(admin.ModelAdmin):
    list_display=('name','cellar', 'year', 'description','price', 'in_our_cellar', )
    list_filter=('cellar','year')


# Register your models here.
admin.site.register(Gallery_image, Gallery_imageAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Contact)


