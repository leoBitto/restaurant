from unittest.util import _MAX_LENGTH
from django.db import models


class Allergen(models.Model):
    name = models.CharField(max_length=100)


class Ingredient(models.Model):
    name=models.CharField(max_length=100)
    supplier = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    

class Producer(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_phone = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.name



# class list
class GroceryList(models.Model):
    name= models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient, blank = True)


# class wine
class Wine(models.Model):
    TYPE_CHOICES = (
    ("RED", "Red"),
    ("BUBBLES", "Bubbles"),
    ("WHITE", "White"),
    ("ROSE", "Rose"),
    ("SWEET", "Sweet"),
    )   

    price = models.FloatField(default=0)
    year = models.IntegerField(default=0)
    name = models.CharField(
        max_length=50,
        default="",
    )
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    grapes = models.CharField(max_length=500, default="",)
    wine_type = models.CharField(
                max_length=20,
                choices=TYPE_CHOICES,
                default="RED",
                )
    zone = models.CharField(max_length = 100, default="", blank=True, null=True)

    order = models.IntegerField(default=0,)
    is_shown=models.BooleanField(default=False,)
    
    class Meta:
        ordering = ['-is_shown',  'wine_type', 'order',]

    def __str__(self):
        return self.name


# class dish
# they compose the menu page
class Dish(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    allergens = models.ManyToManyField(Allergen)
    price = models.FloatField(blank=True, null=True)


    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self):
        return self.name



class Menu(models.Model):
    MENU_TYPE =(
    ("LUNCH", "Lunch"),
    ("DINNER", "Dinner"),
    
    )   


    name=models.CharField(max_length=100, blank=True, null=True, default="Menu")
    from_date = models.DateField()
    to_date = models.DateField()
    dishes = models.ManyToManyField(Dish)
    menu_type = models.CharField(max_length=6, blank=True, null=True, choices=MENU_TYPE)
