from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=16)
    email = models.EmailField(blank=True)
    
    def __unicode__(self):
        return self.name
    
from django.contrib import admin

admin.site.register(Client)
