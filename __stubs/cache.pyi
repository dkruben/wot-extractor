# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import wraps as wraps
from wotdecorators import singleton as singleton
_ZERO_REVISION = 0
_REVISIONS_LOOP = 10

class cached_property(object):
    func: Any
    __doc__: Any
    name: Any
    def __init__(self, func, name=None):
        ...
    def __get__(self, instance, type=None):
        ...

class class_cached_property(object):
    func: Any
    __doc__: Any
    name: Any
    def __init__(self, func):
        ...
    def __get__(self, owner, cls):
        ...

# decorador original: @singleton
class NotMemoized(object):
    ...

class _Nonlocal(object):
    def __init__(self, **kwargs):
        ...

def memoized_method(method=None, isClassCache=False, external=None, key=None):
    ...
def last_cached_method(key=None):
    ...
