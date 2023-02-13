
from django.db import models


# class gallery
class Gallery_image(models.Model):
    header = models.CharField(max_length=100, default="", blank=True, null=True)
    description = models.CharField(max_length=300, default="", blank=True, null=True)
    img = models.ImageField(upload_to="", blank=True, null=True)
    is_first = models.BooleanField(default=False)
    
    def __str__(self):
        return self.header

