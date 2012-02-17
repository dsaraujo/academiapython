# coding: utf-8
# Módulo números de Fibonacci

def fib(n):    # exibe a série de Fibonacci de 0 até n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):   # devolve a série de Fibonacci de 0 até n
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a+b
    return resultado

