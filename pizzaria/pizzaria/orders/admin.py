# coding: utf-8

from django.contrib import admin

from pizzaria.orders.models import Client
from pizzaria.orders.models import Order
from pizzaria.orders.models import Delivery

class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'full_address')
    list_display_links = ('phone', 'name',)
    list_filter = ('district',)
    search_fields = ['phone', 'name', 'address', 'number']

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_date', 'client', 'ready')
    list_display_links = ('order_date', 'client',)
    
    def order_date(self, obj):
        return obj.create_date.strftime('%H:%M')
        
    order_date.short_description = u'time'

admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Delivery)
