# encoding: utf-8

"""Lista de exercícios: listcomps

Para estes exercícios, usaremos as listas abaixo:

mulheres = ['Mariana', 'Ana', 'Paula']
homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']
   
1. Use uma listcomp para gerar uma lista de homens com nomes de 4 ou menos letras.
   
    >>> exercicio1(homens)
    ['Juca', 'Tom']


2. Use uma listcomp para gerar uma lista de duplas (também conhecida em 
computação como uma lista associativa) formada pela letra inicial e o nome 
de cada homem. Por exemplo, a resposta para a lista mulheres seria:

[('M', 'Mariana'), ('A', 'Ana'), ('P', 'Paula')]
   
   
    >>> exercicio2(homens)
    [('P', 'Pedro'), ('J', 'Juca'), ('T', 'Tom'), ('J', 'Joaquim')]
    
    
3. Use o resultado do exercício 2 para gerar um dicionário associando iniciais 
   aos nomes de homens. Quantos itens terá o dicionário assim produzido?
   
    >>> exercicio3(exercicio2(homens))
    {'P': 'Pedro', 'J': 'Joaquim', 'T': 'Tom'}
    >>> len(exercicio3(exercicio2(homens)))
    3

4. Use a função zip para gerar uma lista associativa, e com ela carregar um 
   dicionário associando cada mulher a um homem. Quantos itens terá o dicionário
   assim produzido?
   
    >>> exercicio4(mulheres, homens)
    {'Paula': 'Tom', 'Ana': 'Juca', 'Mariana': 'Pedro'}
    >>> len(exercicio4(mulheres, homens))
    3

5. Bônus: Gere uma lista associativa para organizar uma aula de dança na qual
   todos devem dançar com todos. Quantos casais serão formados?

   Dica: o nome da operação a ser feita neste exercício é produto cartesiano, e
   para fazer isso em uma listcomp ou genexp você precisa usar mais de um for
   dentro da expressão.
   
   >>> exercicio5(mulheres, homens)
   [('Mariana', 'Pedro'), ('Mariana', 'Juca'), ('Mariana', 'Tom'), ('Mariana', 'Joaquim'), ('Ana', 'Pedro'), ('Ana', 'Juca'), ('Ana', 'Tom'), ('Ana', 'Joaquim'), ('Paula', 'Pedro'), ('Paula', 'Juca'), ('Paula', 'Tom'), ('Paula', 'Joaquim')]
   >>> len(exercicio5(mulheres, homens))
   12
   
Vamos retornar 12 pares, 3x4.

6. Bônus: Repita o exercício 5, acrescentando um filtro com if para remover os 
   nomes com menos de 4 letras das duas listas. Quantos casais serão formados?

    >>> exercicio6(mulheres, homens)
    [('Ana', 'Tom')]
    >>> len(exercicio6(mulheres, homens))
    1
    
Só existe um casal onde ambos tem nomes com menos de 4 letras.
    
"""

mulheres = ['Mariana', 'Ana', 'Paula']
homens = ['Pedro', 'Juca', 'Tom', 'Joaquim']

def exercicio1(lista):
    return [i for i in lista if len(i) <5]
    
def exercicio2(lista):
    return [(i[0], i) for i in lista]
    
def exercicio3(lista):
    return {i:j for (i,j) in lista}
    
def exercicio4(m, h):
    l = zip(m, h)
    return {i:j for (i,j) in l}
    
def exercicio5(m, h):
    return [(i,j) for i in m for j in h]
    
def exercicio6(m, h):
    return [(i,j) for i in m if len(i) < 4 for j in h if len(j) < 4]
    

