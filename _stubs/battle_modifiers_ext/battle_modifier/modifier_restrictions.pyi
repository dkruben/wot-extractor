# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/battle_modifier/modifier_restrictions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from future.utils import viewitems as viewitems
from soft_exception import SoftException as SoftException
from battle_modifiers_ext.battle_modifier import modifier_readers as modifier_readers
from battle_modifiers_ext.constants_ext import UseType as UseType, ModifierRestriction as ModifierRestriction, DataType as DataType
from typing import TYPE_CHECKING as TYPE_CHECKING, Any as Any, Set as Set, Dict as Dict, Type as Type, Optional as Optional, Tuple as Tuple
from battle_modifiers_ext.battle_modifier.modifier_filters import ModificationNode as ModificationNode
from ResMgr import DataSection as DataSection
g_modifierValidators: dict

class IModifierValidator(object):
    __slots__: tuple
    arg: _Any
    def __init__(self, config, paramId):
        ...
    def __call__(self, modificationNode):
        ...
    def _readConfig(self, config, paramId):
        ...
    def _validate(self, modificationNode):
        ...
    def _errorMessage(self, modificationNode):
        ...

class UseTypeValidator(IModifierValidator):
    def _readConfig(self, config, _):
        ...
    def _validate(self, modificationNode):
        ...
    def _errorMessage(self, modificationNode):
        ...

class DataTypeValidator(IModifierValidator):
    def __call__(self, modificationNode):
        ...
    def _readConfig(self, _, __):
        ...
    def _validate(self, modificationNode):
        ...

class IValueValidator(IModifierValidator):
    def _readConfig(self, config, paramId):
        ...
    def _validate(self, modificationNode):
        ...
    def _validateValue(self, value):
        ...

class MinValidator(IValueValidator):
    def _validateValue(self, value):
        ...
    def _errorMessage(self, modificationNode):
        ...

class MaxValidator(IValueValidator):
    def _validateValue(self, value):
        ...
    def _errorMessage(self, modificationNode):
        ...

class IValueLimiter(object):
    def __call__(self, value):
        ...

class MinLimiter(IValueLimiter):
    __slots__: tuple
    __min: _Any
    def __init__(self, value):
        ...
    def __call__(self, value):
        ...

class MaxLimiter(IValueLimiter):
    __slots__: tuple
    __max: _Any
    def __init__(self, value):
        ...
    def __call__(self, value):
        ...

class MinMaxLimiter(IValueLimiter):
    __slots__: tuple
    __min: _Any
    __max: _Any
    def __init__(self, minValue, maxValue):
        ...
    def __call__(self, value):
        ...

def readRestrictions(config, paramId, allowedRestrictions=None):
    ...
def getValueLimiter(minValue, maxValue):
    ...
