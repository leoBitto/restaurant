from django.shortcuts import render

from website.models import Gallery_image
from grocer.models import *
# Create your views here.


## landing
def landing(request):

    first_image = Gallery_image.objects.filter(is_first=True).first()
    images = Gallery_image.objects.filter(is_first=False)
    num_of_images = images.count()+1

    context={
        'first_image': first_image,
        'num_of_images': range(1, num_of_images),
        'images':images,
    }

    return render(request, 'website/landing.html', context)


## shop
def shop(request):
    context={}

    return render(request, 'website/shop.html', context)


## wine
def wine(request):
    reds = Wine.objects.filter(is_shown = True, wine_type="RED")
    bubbles = Wine.objects.filter(is_shown = True)
    whites = Wine.objects.filter(is_shown = True)
    roses = Wine.objects.filter(is_shown = True)
    sweets = Wine.objects.filter(is_shown = True)

    context={
        'reds':reds,
        'bubbles':bubbles,
        'whites':whites,
        'roses':roses,
        'sweets':sweets,
        }

    return render(request, 'website/wine.html', context)


## menu
def menu(request):
    dishes = Dish.objects.all()
    context={
        'dishes':dishes,
    }

    return render(request, 'website/menu.html', context)