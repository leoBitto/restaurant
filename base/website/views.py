from django.shortcuts import render

from website.models import *

# Create your views here.


## landing
def landing(request):

    #images NEED TO BE OPTIMIZED
    first_image = Gallery_image.objects.filter(is_first=True).first()
    images = Gallery_image.objects.filter(is_first=False)
    num_of_images = images.count()+1
    
    #contacts
    contacts = Contact.objects.all().first()

    #opening hours
    Openinghour = Opening_hour.objects.all().first()

    context={
        'first_image': first_image,
        'num_of_images': range(1, num_of_images),
        'images':images,

        'contacts':contacts,
        'opening_hours':Openinghour,
    }

    return render(request, 'website/landing.html', context)


## menu
def menu(request):
    dishes = None
    context={
        'dishes':dishes,
    }

    return render(request, 'website/menu.html', context)


## wine
def wine(request):
    wine = Wine.objects.filter(bottles_in_our_cellar__gt = 0)
    
    context={
        'wines':wine,
    }

    return render(request, 'website/wine.html', context)