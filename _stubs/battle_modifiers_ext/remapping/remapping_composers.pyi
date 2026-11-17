# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/remapping/remapping_composers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional, Any as Any, Dict as Dict, List as List, FrozenSet as FrozenSet, Type as Type
from battle_modifiers_ext.constants_ext import ModifiersWithRemapping as ModifiersWithRemapping
from battle_modifiers_common import ModifiersContext as ModifiersContext
from battle_modifiers_ext.remapping.remapping_conditions import IRemappingCondition as IRemappingCondition
_START_PATTERN = '{'
_END_PATTERN = '}'
_DEFAULT_COMPOSERS: dict
_COMPOSERS_FACTORY: dict

class IComposer(object):
    __slots__: tuple
    def getValue(self, ctx, oldValue):
        ...
    def getValues(self, oldValue):
        ...

class _BaseComposer(IComposer):
    __slots__: tuple
    _conditions: _Any
    _targetTemplate: _Any
    _specialRules: _Any
    def __init__(self, conditions, targetTemplate, specialRules):
        ...
    def getValue(self, ctx, oldValue):
        ...
    def getValues(self, oldValue):
        ...
    @classmethod
    def _getItemName(cls, ctx, oldValue):
        ...
    def __applySpecialRules(self, ctx, oldValue):
        ...

class _DefaultGunEffectsComposer(_BaseComposer):
    def getValue(self, ctx, oldValue):
        ...
    @classmethod
    def _getItemName(cls, _, oldValue):
        ...

class _DefaultShotEffectsComposer(_BaseComposer):
    @classmethod
    def _getItemName(cls, _, oldValue):
        ...

class _DefaultGunPrefabEffectsComposer(_BaseComposer):
    @classmethod
    def _getItemName(cls, _, oldValue):
        ...

class _DefaultShotPrefabEffectsComposer(_BaseComposer):
    @classmethod
    def _getItemName(cls, _, oldValue):
        ...

class _DefaultSoundNotificationsComposer(_BaseComposer):
    _REMOVE_NOTIFICATION = 'none'
    def getValue(self, ctx, oldValue):
        ...
    def getValues(self, oldValue):
        ...
    def __applyRemoveRule(self, value):
        ...

class _DefaultExhaustEffectsComposer(_BaseComposer):
    @classmethod
    def _getItemName(cls, _, oldValue):
        ...

def getComposerClass(remappingName, modifierName):
    ...
