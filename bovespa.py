# -*- coding: utf-8 -*-
import os
import pprint

def Papel(object):
    def __init__(self, tick, nome, tipo, valor):
        self._tick = tick.trim()
        self._nome = nome.trim().title()
        self._tipo = tipo.trim()
        self._valor = float(valor) # Depois fazer com Decimal

    def __str__(self):
        return "%s: %d" % (self._tick, self._valor)

def readfile(filename):
    linhas = []
    with open(filename) as f:
        for line in f:
            linhas.append(line.split('\t'))
    return linhas


def processfile(linhas):
    setores = {}
    setor_atual = ''
    for c in linhas:    
        if len(c) == 7: #Inicio de Categoria
            setor_atual = c[0]
            setores[setor_atual] = []
            p = Papel(*c[1:5])
            setores[setor_atual].append(p)
        elif len(c) == 5: # Adição a categoria atual    
            setores[setor_atual].append(c[0:4])
    return setores

if __name__ == '__main__':
    s = processfile(readfile('carteira_ibovespa.txt'))
    pprint.pprint(s)
