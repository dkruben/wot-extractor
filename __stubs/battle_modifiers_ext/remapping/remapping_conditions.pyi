# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/remapping/remapping_conditions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from typing import Dict as Dict, FrozenSet as FrozenSet, TYPE_CHECKING as TYPE_CHECKING
from battle_modifiers_ext.constants_ext import GunCaliber as GunCaliber, ShellCaliber as ShellCaliber, ShellKind as ShellKind, RemappingConditionNames as RemappingConditionNames
from nations import NAMES as NAMES
from battle_modifiers_common import ModifiersContext as ModifiersContext
_CONDITIONS_FACTORY: dict

class IRemappingCondition(object):
    __slots__: tuple
    @classmethod
    def getName(cls):
        ...
    def __call__(self, ctx):
        ...

class _BaseCondition(IRemappingCondition):
    __slots__: tuple
    _CONDITION_NAME = 'baseCondition'
    _remappingName: Any
    _remapping: Any
    def __init__(self, remappingName, remapping):
        ...
    def __call__(self, ctx):
        ...
    @classmethod
    def getName(cls):
        ...
    def _getParam(self, ctx):
        ...

class _RemappingNameCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.REMAPPING_NAME
    def _getParam(self, ctx):
        ...

class _NationCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.NATION
    def _getParam(self, ctx):
        ...

class _OutfitCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.OUTFIT
    def _getParam(self, ctx):
        ...

class _GunNameCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.GUN_NAME
    def _getParam(self, ctx):
        ...

class _GunCaliberCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.GUN_CALIBER
    def _getParam(self, ctx):
        ...

class _ShellKindCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.SHELL_KIND
    def _getParam(self, ctx):
        ...

class _ShellShotsCountCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.SHELL_SHOTS_COUNT
    def _getParam(self, ctx):
        ...

class _ShellCaliberCondition(_BaseCondition):
    __slots__: tuple
    _CONDITION_NAME = RemappingConditionNames.SHELL_CALIBER
    def _getParam(self, ctx):
        ...

def getConditionClass(conditionName):
    ...
