# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/WeakMethod.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from weakref import ref as ref

class WeakMethod(ref):
    __slots__: tuple
    __hash__ = ref.__hash__
    _func_ref: Any
    _meth_type: Any
    _alive: Any
    def __new__(cls, meth, callback=None):
        ...
    def __call__(self):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __repr__(self):
        ...

class WeakMethodProxy(object):
    __nonzero__: Any
    _methodRef: Any
    def __init__(self, method, callback=None):
        ...
    def __call__(self, *args, **kwargs):
        ...
    def __bool__(self):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    def __repr__(self):
        ...
