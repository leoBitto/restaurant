from django.contrib import admin
from .models import *

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
    


class WineAdmin(admin.ModelAdmin):
    list_display=('name',
                'cellar',
                'year',
                'description',
                'price_from_vendor', 
                'price_to_public', 
                'in_our_cellar', )
    list_filter=('cellar','year')


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


# class WebsiteAdminSite(AdminSite):
#     def get_app_list(self, request):
#         """
#         Return a sorted list of all the installed apps that have been
#         registered in this site.
#         """
#         ordering = {
#             "Event heros": 1,
#             "Event villains": 2,
#             "Epics": 3,
#             "Events": 4
#         }
#         app_dict = self._build_app_dict(request)
#         # a.sort(key=lambda x: b.index(x[0]))
#         # Sort the apps alphabetically.
#         app_list = sorted(app_dict.values(), key=lambda x: x['name'].lower())

#         # Sort the models alphabetically within each app.
#         for app in app_list:
#             app['models'].sort(key=lambda x: ordering[x['name']])

#         return app_list