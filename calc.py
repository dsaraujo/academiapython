# coding: utf-8
# Simula uma calculadora de boteco

__author__ = 'Daniel Araujo'

total = 0.0
ops = ['+', '-', '*', '/','**', '%', '//'] # Para extender, adicione expressões aqui
current = ops[0]                           # Inicia a calculadora com soma (ops[0])
while True:
  print total
  p = raw_input(current)
  if not p.strip(): break
  if p == '\x1b':                          # \x1b => tecla Esc
    total = 0
    print 'Clr'                            # Imprime Clr (Clear)
  elif p in ops:
    current = p                            # Troca a operação
  else: 
    try:
      f = str(float(p))
      total = eval('total'+current+f)      # Eval resolve a expressão como um comando
    except ValueError:                     # Jogada por float(str)
      print 'Err:',p                       # Imprime Err (Error)
