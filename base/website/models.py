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
    mail = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return "Contacts"


class Opening_hour(models.Model):
    weekdays = models.CharField(max_length = 200, blank=True, null=True)
    weekend = models.CharField(max_length=300, blank=True, null=True)
    closing_day = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return "Opening hours"


class Entree(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name


class First_dish(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'First_dishes'


class Second_dish(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Second_dishes'


class Side_dish(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Side_dishes'


class Dessert(models.Model):
    name = models.CharField(max_length=100, null=True)
    price = models.FloatField()
    description = models.TextField(blank = True, null = True)

    def __str__(self):
        return f"{self.name}"


class Menu(models.Model):
    
    title = models.CharField(max_length=100, default="Il Nostro Menù", blank=True,)

    entree = models.ManyToManyField(Entree, blank = True)
    first_dish = models.ManyToManyField(First_dish, blank = True)
    second_dish = models.ManyToManyField(Second_dish, blank = True)
    side_dish = models.ManyToManyField(Side_dish, blank = True)
    dessert = models.ManyToManyField(Dessert, blank = True)
    pub_date = models.DateField(auto_now=True, editable=True)
    
    
    class Meta:
        ordering = ['-pub_date']
        verbose_name_plural = 'Menues'
    
    def __str__(self):
        return self.title
    

class Business_Menu(models.Model):
    opzione1 = models.CharField(max_length=300, blank=True)
    opzione2 = models.CharField(max_length=300, blank=True)
    
    class Meta:
        verbose_name_plural = 'Business_Menues'


class Wine(models.Model):
    name = models.CharField(max_length=100, null=True)
    cellar = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null = True)
    price_from_vendor = models.IntegerField()
    price_to_public = models.FloatField()
    bottles_in_our_cellar = models.IntegerField(blank = True, null=True)
    year = models.IntegerField(blank=True, null=True)

    @property
    def earnings_per_bottle(self):
        return self.price_to_public - self.price_from_vendor

    @property
    def total_value(self):
        return self.price_from_vendor * self.bottles_in_our_cellar


    def __str__(self):
        return f"{self.name}, {self.cellar}"

    


