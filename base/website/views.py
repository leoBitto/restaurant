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
    menu = Menu.objects.latest('pub_date')

    entrees = menu.entree.all()
    first_dishes = menu.first_dish.all()
    second_dishes = menu.second_dish.all()
    side_dishes = menu.side_dish.all()
    desserts = menu.dessert.all()

    title = "Il Nostro Menù"

    context={
        'entrees':entrees,
        'first_dishes':first_dishes,
        'second_dishes':second_dishes,
        'side_dishes':side_dishes,
        'desserts':desserts,
        'title':title,
    }

    return render(request, 'website/menu.html', context)


## menu
def business_menu(request):
    menu = Business_Menu.objects.latest('pub_date')
    
    entrees = menu.entree.all()
    first_dishes = menu.first_dish.all()
    second_dishes = menu.second_dish.all()
    side_dishes = menu.side_dish.all()
    desserts = menu.dessert.all()

    title = "Menù del pranzo"
    description = "due portate a scelta 23€"
    description2 = "tre portate a scelta 33€"

    context={
        'entrees':entrees,
        'first_dishes':first_dishes,
        'second_dishes':second_dishes,
        'side_dishes':side_dishes,
        'desserts':desserts,
        'title':title,
        'description':description,
        'description2':description2,
    }

    return render(request, 'website/menu.html', context)


## wine
def wine(request):
    wine = Wine.objects.filter(bottles_in_our_cellar__gt = 0)
    
    context={
        'wines':wine,
    }

    return render(request, 'website/wine.html', context)