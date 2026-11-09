# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/kill_cam_visuals.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import logging as logging
import typing as typing
from typing import List as List
import BigWorld as BigWorld
import CGF as CGF
import Math as Math
import math_utils as math_utils
from cgf_components.highlight_component import HighlightComponent as HighlightComponent
from cgf_components.visual_effect_component_manager import ImpactZoneComponent as ImpactZoneComponent
from dyn_objects_cache import _KillCamEffectDynObjects as _KillCamEffectDynObjects
from functools import partial as partial
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
_BOUND_MODELS_IMPACT_OFFSET = 0.025
_UNSPOTTED_CONE_RANDOM_OFFSET = 5
_UNSPOTTED_CONE_MAX_PITCH = 1077
LINE_WIDTH = 3
_logger: Any
_LENGTH_FACTOR = 2.08
_DOTS_SPACING = 0.06

class EffectsController(CallbackDelayer):
    gameObjects: Any
    __isActive: Any
    __spaceID: Any
    __effectsPathsConfig: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def hideEdges(self):
        ...
    def displayKillCamEffects(self, vehicleAppearance, maxComponentIndex, hasProjectilePierced, hasNonPiercedDamage, isSPG, isSpotted, isShellHE, explosionRadius, trajectoryPoints, segments, impactPoint, isRicochet):
        ...
    def __removeEdgeDrawer(self):
        ...
    def __removeGameObjects(self):
        ...
    def __getLoadCallback(self, callback):
        ...
    def __spawnHitCone(self, hitPosition, originPosition):
        ...
    def __spawnShellTrajectory(self, points, isSpgShot=False, isRicochet=False):
        ...
    def __spawnImpactPoint(self, hitPosition):
        ...
    def __spawnSpacedArmorImpactPoint(self, hitPosition):
        ...
    def __spawnSpacedArmorLine(self, originPosition, hitPosition):
        ...
    def __spawnExplosionSphere(self, position, radius):
        ...
    def __spawnImpactZone(self, segments, vehicleAppearance, maxComponentIndex):
        ...
    @staticmethod
    def __setTransformToGameObject(pending, queue, scale, rotationYPR, position):
        ...
