# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/readers/prefab_effects_readers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import ResMgr as ResMgr
from constants import SHELL_TYPES_INDICES as SHELL_TYPES_INDICES
from debug_utils import LOG_ERROR as LOG_ERROR
from items import _xml as _xml
from items.components import component_constants as component_constants
EffectDesc: Any
ShotEffectItemDesc: Any
EffectDescMap: Any
ShotEffectGroups: Any
GunEffectDesc: Any
GunEffectDescMap: Any
ShotEffectDesc: Any
ShotEffects: Any
DecalDesc: Any
Decals: Any
ShotDefaults: Any
Defaults: Any
_EMPTY_EFFECT: Any
_EMPTY_SHOT_EFFECT_ITEM: Any

def readDefaultPrefabEffects(xmlCtx, section, subsectionName):
    ...
def readGunEffects(xmlPath):
    ...
def readShotEffects(xmlPath, decals):
    ...
def readDecals(xmlPath):
    ...
def _readEffect(xmlCtx, section):
    ...
def _readGunEffect(xmlCtx, section, idx):
    ...
def _readShotEffectItem(xmlCtx, section, decals):
    ...
def _readShotEffect(xmlCtx, section, decals, idx):
    ...
def _readDecal(xmlCtx, section, idx):
    ...
