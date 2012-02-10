#encoding: utf-8
# This file is written in pt_BR

"""Lista de exercícios: set

1. "The quick brown fox jumps over the lazy dog" é um pangrama, uma frase
que usa todas as letras do alfabeto inglês.

O que faz o código abaixo? Qual a resposta que aparece no lugar do marcador «1»?

>>> fox = 'The quick brown fox jumps over the lazy dog.'
>>> fox_letters = set(l.upper() for l in fox if l.isalpha())
>>> len(fox_letters)
«1»

«1» vai ser 26, o tamanho de um set com todas as letras maiúsculas do alfabeto:

set(['A', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'K', 'J', 'M', 'L', 'O', 'N',
 'Q', 'P', 'S', 'R', 'U', 'T', 'W', 'V', 'Y', 'X', 'Z'])

"""



"""
2. Que resposta apareceria no lugar de «1» se não fosse usado o filtro if
na expressão geradora acima?

28, pois não filtrariamos os espaços e o ponto final.

"""


"""
3. Para verificar se o conjunto fox_letters realmente contém todas as letras do
alfabeto, podemos verificar se este conjunto é igual ao conjunto das letras 
ASCII maíusculas que o Python conhece. Para fazer esta verificação, o que 
devemos escrever no lugar de «1», e que resposta aparecerá em «2»?

>>> import string
>>> letters = set(string.ascii_uppercase)
>>> fox_letters == «1»
«2»

Pode simples como fox_letters == letters, voltando True.

Outra maneira seria fox_letters.difference(letters) voltar vazio set([]), ou 
seja, não existem items que estão em fox_letters mas não estão em letters.

"""

"""
4. O alfabeto português antigamente era menor que o inglês, mas hoje é igual
(tirando o cedilha). A frase abaixo aparece como exemplo de pangrama na 
Wikipédia em português, vamos verificar usando a mesma técnica usada acima, 
substituindo «1», «2» e «3» pelas expressões apropriadas:

>>> jabuti = 'Um pequeno jabuti xereta viu dez cegonhas felizes.'
>>> jabuti_letras = set(«1» for l in «2» if «3»)
Uma vez que temos o conjunto das letras da frase do jabuti, podemos verificar
a diferença entre o conjunto de todas as letras e este conjunto. Qual operador
usamos em «1» e qual a resposta aparecerá em «2»:

>>> letters «1» jabuti_letras
set(«2»)

operador de menos -, com o resultado set(['Y', 'K', 'W']). Representa os itens 
de letters exceto os itens de jabuti_letras

"""


"""
4.1. Bônus: Existem dois operadores de conjunto que podem ser usados no lugar
de «1», e neste exemplo ambos produziriam o mesmo resultado em «2». Quais são os
operadores, e qual a diferença entre eles?

^ retorna o mesmo resultado, mas volta itens que são unicos de cada set


"""
