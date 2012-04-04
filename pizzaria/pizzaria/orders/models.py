# coding: utf-8
from django.db import models

# Create your models here.

import num2eng

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
        ordering = ['phone', 'ext']
    
    def __unicode__(self):
        p = self.phone
        if self.ext:
            p += ' ex %s' % self.ext
        return u'%s - %s' % (p, self.name)
    
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
    
    list_select_related = True # Do JOINs and less queries to this admin

    def __unicode__(self):
        c = len(self.pizza_set.all())
        return u'%s pizza%s to %s @ %s' % (num2eng.num2eng(c), 's' if c > 1 else '', self.client, self.create_date.strftime('%H:%M'))

class Delivery(models.Model):
    name = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = u'Delivery Guys'
    
    def __unicode__(self):
        return self.name

FLAVORS = [
    ('cheese', 'Cheese'),
    ('pepperoni', 'Pepperoni'),
    ('margherita', 'Margherita'),
    ('tuscani', 'Tuscani'),
    ('roastbeef', 'Roast Beef'),
]
        
class Pizza(models.Model):
    order = models.ForeignKey(Order)
    flavor1 = models.CharField(u'flavor', max_length=32, choices=FLAVORS)
    flavor2 = models.CharField(u'flavor 2', max_length=32, choices=FLAVORS, blank=True)
    notes = models.TextField(blank=True)
    
    def __unicode__(self):
        f = u'Full %s' % self.flavor1
        if self.flavor2:
            f = u'½ %s ½ %s' % (self.flavor1, self.flavor2)
        return f
        
        

