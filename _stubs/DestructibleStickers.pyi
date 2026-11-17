# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/DestructibleStickers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import CGF as CGF
import GpuDecals as GpuDecals
import math_utils as math_utils
import VehicleStickers as VehicleStickers
from VehicleEffects import DamageFromShotDecoder as DamageFromShotDecoder
from constants import VEHICLE_HIT_EFFECT as VEHICLE_HIT_EFFECT
from items.components.component_constants import INVALID_EFFECT_INDEX as INVALID_EFFECT_INDEX
from helpers.prefab_effects import resolvePrefabStickerID as resolvePrefabStickerID, resolveDamageStickerPrefab as resolveDamageStickerPrefab
from cgf_modules import game_events as game_events
from VehicleStickers import DamageStickerData as DamageStickerData
from Compound import Compound as Compound
_logger: Any

class DestructibleStickers(object):
    __LOD_DISTANCE = 1000.0
    __model: Any
    __gameObject: Any
    __stickerModel: Any
    __nodeToAttach: Any
    __damageStickers: Any
    __parametrizedDamageStickers: Any
    def __init__(self, spaceID, compound, partIdx, gameObject):
        ...
    def destroy(self):
        ...
    def addDamageSticker(self, code, stickerID, prefabEffIndex, data, collisionComponent, isActive):
        ...
    def delDamageSticker(self, code):
        ...
    def __addParametrizedDamageSticker(self, code, prefabEffIndex, hitType, data, collisionComponent, isActive):
        ...
    def __addLegacyDamageSticker(self, code, stickerID, data):
        ...
    def __delLegacyDamageSticker(self, damageSticker):
        ...
