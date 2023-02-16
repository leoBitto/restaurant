from django.contrib import admin
from .models import *
from django.db.models import Sum

class Gallery_imageAdmin(admin.ModelAdmin):
    list_display=('header', 'description', 'is_first', 'show_image')


class EntreeAdmin(admin.ModelAdmin):
    list_display=('name', 
                'price', 
                'description', )
    search_fields=("name", )


class FirstAdmin(admin.ModelAdmin):
    list_display=('name', 
                'price', 
                'description', )
    search_fields=("name", )


class SecondAdmin(admin.ModelAdmin):
    list_display=('name', 
                'price', 
                'description', )
    search_fields=("name", )
    


class SideAdmin(admin.ModelAdmin):
    list_display=('name', 
                'price', 
                'description', )
    search_fields=("name", )
    


class DessertAdmin(admin.ModelAdmin):
    list_display=('name', 
                'price', 
                'description', )
    search_fields=("name", )
    


class MenuAdmin(admin.ModelAdmin):
    list_display=('id','pub_date')
    raw_id_fields = ["dessert"]
    
    


class WineAdmin(admin.ModelAdmin):

    class IsInStockFilter(admin.SimpleListFilter):
        title='is_in_stock'
        parameter_name = 'is_in_stock'

        def lookups(self, request, model_admin):
            return (
                ('Yes', 'Yes'),
                ('No', 'No'),
            )

        def queryset(self, request, queryset):
            value = self.value()
            if value == 'Yes':
                return queryset.filter(bottles_in_our_cellar__gt = 0 )
            elif value == 'No':
                return queryset.exclude(bottles_in_our_cellar__gt = 0)
            else:
                queryset


    def earnings_per_bottle(self, obj):
        return obj.price_to_public - obj.price_from_vendor

    def total_value(self, obj):
        return obj.price_from_vendor * obj.bottles_in_our_cellar

    def is_in_stock(self, obj):
        return obj.bottles_in_our_cellar > 0

    is_in_stock.boolean = True

    
    list_display=(
                'name',
                'cellar',
                'year',
                'price_from_vendor', 
                'price_to_public', 
                'bottles_in_our_cellar',
                'earnings_per_bottle',
                'total_value',
                'is_in_stock',
                
                )

    list_filter=(
        'cellar',
        'year', 
        IsInStockFilter,
    )
    



# Register your models here.
admin.site.register(Gallery_image, Gallery_imageAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Entree, EntreeAdmin)
admin.site.register(First_dish, FirstAdmin)
admin.site.register(Second_dish, SecondAdmin)
admin.site.register(Side_dish, SideAdmin)
admin.site.register(Dessert, DessertAdmin)
admin.site.register(Wine, WineAdmin)
admin.site.register(Contact)
admin.site.register(Opening_hour)



