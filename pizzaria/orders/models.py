# coding: utf-8
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=16, db_index=True)
    ext = models.CharField(max_length=8, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=64, db_index=True)
    number = models.PositiveIntegerField(u'número', db_index=True)
    district = models.CharField(max_length=64, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('phone', 'ext')
    
    def __unicode__(self):
        return self.name
    

