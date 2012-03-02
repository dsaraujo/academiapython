# -*- coding: utf-8 -*-
from decimal import Decimal

"""Classe que define um papel da bolsa"""
class Papel(object):
    def __init__(self, tick, nome, tipo, valor):
        """Inicia um novo papel
          tick - A abreviação da ação
          nome - O nome extenso da ação
          tipo - O tipo de ação
          valor - O valor, no formato 1.000,00 guardado como float"""
        self._tick = tick.strip()
        self._nome = nome.strip().title()
        self._tipo = tipo.strip()
        self._valor = float(valor.replace('.','').replace(',', '.'))

    def __str__(self):
        return "%s: %d" % (self._tick, self._valor)
      
    def __repr__(self):
        return "<Papel %s>" % self._tick

"""Classe que define um papel da bolsa com valor em Decimal"""
class PapelDecimal(Papel):
  
    def __init__(self, tick, nome, tipo, valor):
        """Inicia um novo papel
          tick - A abreviação da ação
          nome - O nome extenso da ação
          tipo - O tipo de ação
          valor - O valor, no formato 1.000,00 guardado como Decimal"""
        Papel.__init__(self, tick, nome, tipo, valor)
        v = valor.replace('.','').replace(',', '.')
        self._valor = Decimal(v)

def readfile(filename):
    """Le um arquivo texto da bolsa e divide as linhas por tabs.
      Retorna uma lista de listas"""
    linhas = []
    with open(filename) as f:
        for line in f:
            linhas.append(line.split('\t'))
    return linhas

def processfile(linhas, classe=Papel):
    """Processa uma lista de listas, no formato abaixo, e retorna um dicionario
    de dados, com o nome do setor como chave, e uma lista de objetos Papel como
    valor.
    
    linhas - lista de listas, onde as listas podem conter sete elementos, 
             quando definir um setor, ou cinco, quando fizer parte do último
             setor definido
    classe - Qual classe será armazenada no dicionário, o padrão é Papel, mas
             pode ser usado PapelDecimal"""
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
    """Processa um dicionario de stores, retornando um dicionário com a soma
    dos totais dos valores dos papeis como valor, e o nome do setor como 
    chave."""
    sum_sect = {}
    for s in setores.keys():
      papeis = setores[s]
      sum_sect[s] = sum([p._valor for p in papeis])
    return sum_sect
      
def compare(s1, s2):
    """Imprime na tela a diferença entre dois dicionarios de somas de setor,
    usando as chaves do primeiro como referencia"""
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