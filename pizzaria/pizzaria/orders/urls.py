from django.conf.urls import patterns, include, url

from .views import right_now
from .views import list_pizzas

urlpatterns = patterns('',
    url(r'now$', right_now, name='now'),
    url(r'pizzas$', list_pizzas, name='list_pizzas'),
)
