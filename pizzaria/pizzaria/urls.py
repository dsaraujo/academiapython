from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from pizzaria.orders.views import right_now

urlpatterns = patterns('',
    url(r'^ord/', include('pizzaria.orders.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
