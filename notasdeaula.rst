Notas de Aula da Academia Python
================================

Aula 1, 2, 3
------------

* sem notas, mal aí.

Aula 4 (2012-01-31)
-------------------

* *xxd*: Aplicativo Unix para ver os bytes de um arquivo
* codecs: modulo Python que codifica e decodifica pra você
    * Unicode: representa através de codepoints
    * UTF-8: Uma maneira de codificar codepoints para bytes (encode)
* Vimos alguns tipos diferentes de IDEs / editores
* Falamos de orientação à objetos e frameworks
* self não é palavra reservada, é só uma convenção (tão comum que editores de
  texto reconhecem com frequência
* __repr__ -> Usado para uso interno numa conversão pra String
* __str__ -> Conversão pra String, similar a *.toString()* do Java
* Variaveis definidas numa classe são variáveis "estáticas" [1]_

.. [1] (not really, mas serve como definição geral)

Aula 5 (2012-02-02)
-------------------

* Falamos das discussões da lista (humano, calculadora)
* **@property**, **@classmethod** e outros decorators (não detalhados ainda)
* global pode ser usada para referenciar uma variável do contexto externo
* Vimos o Relogio do Tkinter com OO
* Para ter herança múltipla: class(pai1, pai2, pai3) C:
* A ordem das super classes é relevante para a resolução dos métodos: o Python
  tenta buscar primeiro métodos em pai1, depois pai2, etc.
* Fizemos um mini dojo com uma calculadora pós-fixa

* Camiseta Python: 
  http://www.linuxmall.com.br/produto/camiseta-python-preta-.html

Aula 6 (2012-02-07)
-------------------

* Todo atributo de classe deve ser imutável. Ou feita uma cópia na inicialização
* Não use um parametro default mutável: ele será sempre associado ao objeto
  função. Se precisar, uma técnica é usar o default *None*, e testar por isso
  para inicializar um novo objeto.
* Você pode proteger o acesso acidental a um atributo usando __ (dunder) antes 
  de uma variável. Isso porque uma variavel da Classe __x vira _Classe__x 
  internamente, protegendo de uma eventual sobrescrita.

Aula 7 (2012-02-09)  
-------------------

* Corrigimos as listas 1 e 2.
* Falamos (muito) sobre iteráveis, iteradores, geradores e afins
* Slides de NoSQL / Isis

Aula 8 (2012-02-14)
-------------------

* Meta programação
* Django
** virtualenv --no-site-packages django1.3
** cd django1.3/bin
** . activate
** cd ..
** pip install django
** django-admin startproject project
** cd project
** chmod +x manage.py
** manage.py runserver
* Descriptors
** guardamos os tipos basicos, mas com setters e getters para os campos
** Depois de muito Django, fizemos um exemplo de itens de um pedido
** Uso de @property
