# encoding: utf-8
from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    active = models.BooleanField(default=True)
    email_user = models.EmailField()

    def __unicode__(self):    
        s = [self.title, ' (', self.description[:30]]
        if len(self.description) > 30: s.append('...')
        s.append(')')
        return ''.join(s)

from django.contrib import admin

admin.site.register(Event)
