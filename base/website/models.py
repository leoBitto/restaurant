from django.db import models
from django.utils.html import format_html

### information models
class Gallery_image(models.Model):
    header = models.CharField(max_length=100, default="", blank=True, null=True)
    description = models.CharField(max_length=300, default="", blank=True, null=True)
    img = models.ImageField(upload_to="", blank=True, null=True)
    is_first = models.BooleanField(default=False)
    
    def __str__(self):
        return self.header

    def show_image(self):
        return format_html('<img src="{}" style="height:100px;" />', self.img.url)


class Contact(models.Model):
    phone = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=50, blank=True, null=True)



### 
class Dish(models.Model):

    choices = (
        (ENTREE := "ENTREE", 'Entree'),
        (FIRST  := "FIRST", 'First'),
        (SECOND  := "SECOND", 'Second'),
        (SIDE  := "SIDE", 'Side'),
        (SWEET  := "SWEET", 'Sweet'),
    )
        
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    description = models.TextField()
    type = models.CharField(max_length=10, choices=choices, default=ENTREE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Dishes'


class Menu(models.Model):
    is_lunch = models.BooleanField(default=False)
    dishes = models.ManyToManyField(Dish)
    pub_date = models.DateField(auto_now=True, editable=True)
    

    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Menues'
    

class Wine(models.Model):
    name = models.CharField(max_length=100, null=True)
    cellar = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    price = models.FloatField()
    in_our_cellar = models.IntegerField(blank = True, null=True)
    year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}, {self.cellar}"
