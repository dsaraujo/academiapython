# coding: utf-8

def exibir(text, estilo=None, cor='preto'):
    if estilo: print '<%s>%s</%s>' % (estilo, text, estilo)
    else: print text

exibir('abacaxi')
exibir('abacaxi','negrito','amarelo')
exibir('abacaxi',cor='azul')

