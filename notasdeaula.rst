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

    1. virtualenv --no-site-packages django1.3
    2. cd django1.3/bin
    3. . activate
    4. cd ..
    5. pip install django
    6. django-admin startproject project
    7. cd project
    8. chmod +x manage.py
    9. manage.py runserver
    
* Descriptors
    * guardamos os tipos basicos, mas com setters e getters para os campos
    * Depois de muito Django, fizemos um exemplo de itens de um pedido
    * Uso de @property
    
Aula 9 (2012-02-16)
-------------------

* http://turing.com.br/material/ppqsp
* Mais um pouco de metaprogramação
* **Lembrete**: tudo isso de metaprogramação requer *new style* classes.
* Tutorial Traduzido em http://turing.com.br/pydoc/2.7
* Falamos de módulos, pacotes, dir(), os.path, __init__.py
* O repr() deveria ser capaz de avaliar o resultado e reconstruir o objeto
  (mas nem sempre é assim, pode atrapalhar mais que ajudar)
* Falamos de *var, **kwvar
* Falamos de I/O de arquivos
* Uso de codecs.open() e io.open()
* módulo **pickle**

Aula 10 (2012-03-01) - Aula bônus
---------------------------------

* O pessoal contou de suas experiências com Python até então;
* Falamos de piramid ( http://docs.pylonsproject.org/projects/pyramid/en/1.3-branch/index.html )
* Mais metaprogramação
* Falamos de lxml (para criação de arquivos XML)
* Mais um pouco do Tutorial Python
* Expressões regulares
* http://pythonregex.com/
* Representações de floats
* Outros exemplos (Bolsa)

Modulo III
==========

Aula 11 (2012-03-20)
--------------------

* Django!
* Fazendo o setup do ambiente (ver Aula 8)

# virtualenv --no-site-packages envname
# source envname/bin/activate

* Use deactivate para sair do ambiente

# pip install django

* Podemos testar com:

>>> import django

# git init . 
# django-admin.py startproject pizzaria
# chmod +x manage.py
# ./manage.py runserver

 Validating models...

 0 errors found
 Django version 1.3.1, using settings 'pizzaria.settings'
 Development server is running at http://127.0.0.1:8000/
 Quit the server with CONTROL-C.

# ./manage startapp orders

* Documentação: https://docs.djangoproject.com/en/1.3/

Aula 12 (2012-03-22)
--------------------

* https://github.com/acpy/modulo3
* Conceitos de Django
* ./manage.py inspectdb -> mostra o banco em formato de models.py
* ./manage.py sqlall app -> mostra o SQL para criar o banco atual
* ./manage.py dumpdata app --indent=2

* Mini aula de Git

* Fixtures
* DICA = tupla de um ('item',)
* Tipos de Fields para Models
* 

Aula 13 (2012-03-27)
--------------------

* Update para Django1.4
** Estrutura do Projeto mudou (mas não muito)
** Migramos para um env novo
** git mv pizzaria pizzaria0

* geramos dados iniciais
* Customizamos o Admin
* Criamos outros modelos

* Setting (use TZ=False) para o uso de Time Zone genérico

Aula 14 (2012-03-29)
--------------------

* Descobri https://www.alwaysdata.com/ -> Host com Django 1.4 gratuito
* Fazer deployment em Apache é trampo!
* OneToOneField(Model) para relações 1:1
* ManyToMany para relações n:m, com tabela intermediária
* Inline in Admin
* sphinx
* Mais opções de Admin

Aula 15 (2012-04-03)
--------------------

* Django ORM
* Managers
* select_related
* Criterios
* Views

Other notes
-----------

* http://forum.xda-developers.com/archive/index.php/t-517308.html
