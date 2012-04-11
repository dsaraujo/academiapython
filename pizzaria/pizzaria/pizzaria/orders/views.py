# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Pizza

import datetime

def right_now(request):
    now = datetime.datetime.now()
    html = '<html><body><h1>Now: %s</h1></body></html>' % now
    return HttpResponse(html)
    
class NowView(TemplateView):
    template_name = 'orders/now.html'
    
    def get_context_data(self, **kwargs):
        context = super(NowView, self).get_context_data(**kwargs)
        context['now'] = datetime.datetime.now().strftime('%H:%M:%S')
        return context
    
def list_pizzas_raw(request):
    plist = []
    for pizza in Pizza.objects.all():
        plist.append(unicode(pizza))
    plist = u'\n'.join(plist)
    html = u'<html><body><h1>Pending Pizzas</h1>'
    html += u'<pre>{0}</pre>'.format(plist)
    html += u'</body></html>' 
    return HttpResponse(html)
    
def list_pizzas(request):
    pizza_list = Pizza.objects.all()
    return render(request, 
                  'orders/pizzas.html', 
                  {'pizza_list': pizza_list},
                  content_type='text/html')
