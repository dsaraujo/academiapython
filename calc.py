# coding: utf-8
# Simula uma calculadora (extensível) de boteco

import operator as op # Usando operator pra facilitar a vida

__author__ = 'Daniel Araujo'

def menosPorcento(a,b):
  return a-(a*(b/100))

def maisPorcento(a,b):
  return a+(a*(b/100))

total = 0.0
ops = {'+':op.add, '-':op.sub, '*':op.mul, '/':op.div,'**':op.pow}
 
ops['-%'] = menosPorcento                  # Para extender, adicione expressões desta maneira
ops['+%'] = maisPorcento

current = '+'                              # Inicia a calculadora com soma (ops[0])
while True:
  print total
  p = raw_input(current)
  if not p.strip(): break
  if p == '\x1b':                          # \x1b => tecla Esc
    total = 0
    print 'Clr'                            # Imprime Clr (Clear) e volta pra soma
    current = '+'
  elif p in ops:
    current = p                            # Troca a operação
  else: 
    try:
      f = float(p)
      total = ops[current](total, f)       # Eval resolve a expressão como um comando
    except ValueError:                     # Jogada por float(str)
      print 'Err:',p                       # Imprime Err (Error)
