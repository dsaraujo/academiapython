# coding: utf-8

from django.contrib import admin

from pizzaria.orders.models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ('phone', 'name', 'full_address')
    list_display_links = ('phone', 'name',)
    list_filter = ('district',)
    search_fields = ['phone', 'name', 'address', 'number']

class PizzaAdmin(admin.TabularInline):
    model = Pizza
    # exclude = ('notes',) # Se quiser esconder no field

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'ready', 'on_the_run')
    list_display_links = ('order',)    
    list_select_related = True # Try to do Joins
    date_hierarchy = 'create_date'
    
    def order(self, obj):
        return obj.__unicode__()
    
    def order_date(self, obj):
        return obj.create_date.strftime('%H:%M')
        
    order_date.short_description = u'time'
    
    def on_the_run(self, obj):
        return bool(obj.ready and obj.delivery and obj.leave_time)
        
    on_the_run.boolean = True
    
    inlines = [PizzaAdmin]

admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Delivery)

