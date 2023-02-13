from django.shortcuts import render

from website.models import Gallery_image

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


## menu
def menu(request):
    dishes = None
    context={
        'dishes':dishes,
    }

    return render(request, 'website/menu.html', context)