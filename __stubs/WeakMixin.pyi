# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/WeakMixin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import weakref as weakref
from inspect import getmodule as getmodule
from future.utils import viewitems as viewitems

class Tapped(object):
    __slots__: tuple
    def tap(self, *appliers, **props):
        ...

class WeakMixin(object):
    def __new__(cls, src, *args, **kwargs):
        ...
    def __init__(self, src, *args, **kwargs):
        ...
    def __getattribute__(self, name):
        ...
