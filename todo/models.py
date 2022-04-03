from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=1000,blank=True,default="")
    order = models.IntegerField(blank=True,default=0)
    completed = models.BooleanField(blank=True,default=False)  
    url = models.CharField(blank=True,max_length=1000,null=True)
    