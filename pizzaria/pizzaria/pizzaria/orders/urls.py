from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView

from .views import right_now, list_pizzas, NowView
from .models import Pizza, Client

urlpatterns = patterns('',
    url(r'now$', NowView.as_view(), name='now'),
    
    url(r'pizzas$', ListView.as_view(model=Pizza,
                                     context_object_name='list_pizzas'),
        name='pizzas-page'),
                                     
    url(r'clients$', ListView.as_view(model=Client,
                                      context_object_name='list_clients'), 
        name='clients-page'),
    url(r'client/(?P<pk>\d+)$',
        DetailView.as_view(model=Client, context_object_name='client'),
        name='info-cli'),
    
)
