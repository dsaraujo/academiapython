# coding: utf-8
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=128)
    phone = models.CharField(u'telephone number',max_length=16, db_index=True)
    ext = models.CharField(max_length=8, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=64, db_index=True)
    number = models.PositiveIntegerField(db_index=True)
    district = models.CharField(max_length=64, blank=True)
    notes = models.TextField(blank=True)
    
    class Meta:
        unique_together = ('phone', 'ext')
    
    def __unicode__(self):
        return self.name
    
    def full_address(self):
        return u'%s, %s' % (self.address, self.number)
        
    full_address.short_description = u'address'
    
class Order(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client)
    ready = models.BooleanField(default=False)
    delivery = models.ForeignKey('Delivery', null=True, 
                                  blank=True, verbose_name='delivery guy')
    leave_time = models.TimeField(null=True, blank=True)

    def __unicode__(self):
        return u'Order of %s' % (self.client)

class Delivery(models.Model):
    name = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = u'Delivery Guys'
    
    def __unicode__(self):
        return self.name
