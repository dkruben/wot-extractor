# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/true_dict/wrap.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import Any as Any
from .core import TrueDict as TrueDict
FixedDict = Any
instance: _Any

class MemberProxy(object):
    memberName: _Any
    def __init__(self, memberName):
        ...
    def __get__(self, inst, owner):
        ...
    def __set__(self, inst, value):
        ...
    def __delete__(self, inst):
        ...

class TrueDictWrapped(TrueDict):
    keysProxy: _Any
    valuesProxy: _Any
    fixedDict: _Any
    def __init__(self, fixedDict):
        ...

class TrueDictConverter(object):
    def createObjFromDict(self, fixedDict):
        ...
    def getDictFromObj(self, obj):
        ...
    def isSameType(self, obj):
        ...
