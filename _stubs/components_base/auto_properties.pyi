# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/components_base/auto_properties.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any

class AutoProperty(object):
    fieldName: Any
    def __init__(self, fieldName=None):
        ...
    def __get__(self, instance, owner=None):
        ...
    def __set__(self, instance, value):
        ...

class TypedProperty(AutoProperty):
    allowedType: Any
    def __init__(self, allowedType, fieldName=None):
        ...
    def __set__(self, instance, value):
        ...

class LinkDescriptor(AutoProperty):
    def __init__(self, fieldName=None):
        ...
    def __set__(self, instance, value):
        ...
    def __call__(self, *args, **kwargs):
        ...

class AutoPropertyInitMetaclass(type):
    def __new__(cls, name, bases, attributes):
        ...
