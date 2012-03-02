# -*- coding: utf-8 -*-
from decimal import Decimal

class Papel(object):
    def __init__(self, tick, nome, tipo, valor):
        self._tick = tick.strip()
        self._nome = nome.strip().title()
        self._tipo = tipo.strip()
        self._valor = float(valor.replace('.','').replace(',', '.'))

    def __str__(self):
        return "%s: %d" % (self._tick, self._valor)
      
    def __repr__(self):
        return "<Papel %s>" % self._tick
      
class PapelDecimal(Papel):
    def __init__(self, tick, nome, tipo, valor):
        Papel.__init__(self, tick, nome, tipo, valor)
        v = valor.replace('.','').replace(',', '.')
        self._valor = Decimal(v)

def readfile(filename):
    linhas = []
    with open(filename) as f:
        for line in f:
            linhas.append(line.split('\t'))
    return linhas

def processfile(linhas, classe=Papel):
    setores = {}
    setor_atual = ''
    for c in linhas:    
        if len(c) == 7: #Inicio de Categoria
            setor_atual = unicode(c[0], "utf-8")
            setores[setor_atual] = []
            p = classe(*c[1:5])
            setores[setor_atual].append(p)
        elif len(c) == 5: # Adição a categoria atual    
            p = classe(*c[0:4])
            setores[setor_atual].append(p)
    return setores

def get_sum_setores(setores):
    sum_sect = {}
    for s in setores.keys():
      papeis = setores[s]
      sum_sect[s] = sum([p._valor for p in papeis])
    return sum_sect
      
def compare(s1, s2):
    print('{:<50} {:<15} {:<15}'.format('Carteira', 'Float', 'Decimal'))
    for k in s1.keys():
        print(' '.join([k.ljust(50), 
                    str(s1[k]).ljust(15), 
                    str(s2[k]).ljust(15)]))
    
if __name__ == '__main__':
    l = readfile('carteira_ibovespa.txt')
    s1 = processfile(l, Papel)
    f1 = get_sum_setores(s1)
    s2 = processfile(l, PapelDecimal)
    f2 = get_sum_setores(s2)
    compare(f1, f2)