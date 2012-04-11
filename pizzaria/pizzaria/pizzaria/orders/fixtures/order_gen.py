#encoding: utf-8

'''[
  {
    "pk": 1, 
    "model": "orders.client", 
    "fields": {
      "name": "Iara Silveira", 
      "district": "Pinheiros", 
      "notes": "Pr\u00f3ximo ao Metr\u00f4", 
      "number": 509, 
      "phone": "11 2367 6659", 
      "ext": "", 
      "address": "R. Fern\u00e3o Dias", 
      "email": ""
    }
  }
  ]
'''

from random import randint, choice
import cfnamegen

records = []
for i in range(20):
    f = dict(ext='', email='', notes='', district='',
                  name = cfnamegen.nameGen(cfnamegen.fooGrammar),
                  phone = '555-%04d' % randint(0,9999),
                  number = (i*10) + 100,
                  address = str(i+4)+'th Street')
    r = dict(pk=i, model='orders.client', fields=f)
    records.append(r)
    
import json
import sys

json.dump(records, sys.stdout, indent=2)
