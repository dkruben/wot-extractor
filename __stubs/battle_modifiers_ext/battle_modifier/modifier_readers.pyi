# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/battle_modifier/modifier_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from math import radians as radians, degrees as degrees
import typing as typing
from battle_modifiers_common.battle_modifiers import BattleParams as BattleParams
from battle_modifiers_ext.battle_modifier.modifier_helpers import makeUseTypeMethods as makeUseTypeMethods
from battle_modifiers_ext.constants_ext import DataType as DataType, UseType as UseType
from bonus_caps_overrides import readBonusCapsOverrides as readBonusCapsOverrides
from constants import DamageAbsorptionLabelToType as DamageAbsorptionLabelToType
from crystal_rewards_common import readCrystalRewards as readCrystalRewards
from items.components.component_constants import KMH_TO_MS as KMH_TO_MS, MS_TO_KMH as MS_TO_KMH
from items.readers import gun_readers as gun_readers
from post_mortem_common import readPostMortemSection as readPostMortemSection
from constants import ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES
from soft_exception import SoftException as SoftException
from ResMgr import DataSection as DataSection
g_cache: dict
_readInt: Any
_readFloat: Any
_readString: Any
_readDict: Any
_dataTypeReaders: dict
_readToDegrees: Any
_readToRadians: Any
_radiansType: dict
_readToKMH: Any
_readToMS: Any
_speedType: dict
_damageAbsorptionReader: Any
_customReaders: dict

def _readVisualScriptPlan(dataSection):
    ...
def _readGoldReserveGains(section):
    ...
def registerParamReaders(paramId, dataType):
    ...
