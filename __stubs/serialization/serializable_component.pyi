# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/serialization/serializable_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from collections import OrderedDict as OrderedDict
from future.utils import iteritems as iteritems
from typing import MutableMapping as MutableMapping, Any as Any, TypeVar as TypeVar
import Math as Math
from .definitions import FieldTypes as FieldTypes, FieldFlags as FieldFlags, FieldType as FieldType
from py2to3.moves.io import FastStringIO as FastStringIO
__all__: tuple
SerializableComponentChildType: _Any

class SerializableComponent(object):
    fields: _Any
    __slots__: tuple
    customType = None
    preview = False
    def __eq(self, other, ignoreFlags):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    def __repr__(self):
        ...
    def weak_eq(self, other):
        ...
    def copy(self):
        ...
    def isFilled(self):
        ...
    def __writeStr(self, stream):
        ...
    def to_dict(self):
        ...
