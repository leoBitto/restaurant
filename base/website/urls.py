from django.urls import path
from website import views


urlpatterns = [
    path('', views.landing, name="landing"),
    path('menu', views.menu, name="menu"),
    path('business_menu', views.business_menu, name="business_menu"),
    path('wine', views.wine, name="wine"),
]