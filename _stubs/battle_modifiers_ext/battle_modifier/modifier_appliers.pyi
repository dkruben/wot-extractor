# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/battle_modifier/modifier_appliers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import copy as copy
from future.utils import viewitems as viewitems
from itertools import chain as chain
from typing import Any as Any, Dict as Dict, List as List, Optional as Optional, TYPE_CHECKING as TYPE_CHECKING, Union as Union
from battle_modifiers_common.battle_modifiers import BattleParams as BattleParams
from battle_modifiers_ext import remappings_cache as remappings_cache
from battle_modifiers_ext.battle_modifier.modifier_helpers import makeUseTypeMethods as makeUseTypeMethods
from battle_modifiers_ext.constants_ext import ModifiersWithRemapping as ModifiersWithRemapping, DataType as DataType, UseType as UseType
from constants import VEHICLE_HEALTH_DECIMALS as VEHICLE_HEALTH_DECIMALS
from items.components.sound_components import WWTripleSoundConfig as WWTripleSoundConfig
from items.components.shell_components import Stun as Stun
from math_common import ceilTo as ceilTo, round_py2_style_int as round_py2_style_int
from battle_modifiers_common.battle_modifiers import ModifiersContext as ModifiersContext
g_cache: dict
_defaultVal: _Any
_defaultMul: _Any
_defaultAdd: _Any
_dataTypeAppliers: dict
_customAppliers: dict

def _shotEffectsApplier(value, paramVal, ctx=None):
    ...
def _gunEffectsApplier(value, paramVal, ctx=None):
    ...
def _shotPrefabEffectsApplier(value, paramVal, ctx=None):
    ...
def _gunPrefabEffectsApplier(value, paramVal, ctx=None):
    ...
def _gunPrefabsApplier(value, paramVal, ctx=None):
    ...
def _rootPrefabsMechanicEffectsApplier(value, paramVal, ctx=None):
    ...
def _engineSoundsApplier(_, paramVal, __=None):
    ...
def _exhaustEffectsApplier(value, paramVal, ctx=None):
    ...
def _soundNotificationsApplier(value, paramVal, ctx=None):
    ...
def _vehicleEffectsApplier(value, paramVal, ctx=None):
    ...
def _shellStunApplier(value, paramVal, ctx=None):
    ...
def registerParamAppliers(paramId, dataType):
    ...
