# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/battleground/berserker_effect.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import CGF as CGF
import AnimationSequence as AnimationSequence
import Math as Math
import math_utils as math_utils
import ResMgr as ResMgr
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from components_base.component_controller import ComponentController as ComponentController
from helpers import dependency as dependency, newFakeModel as newFakeModel, CallbackDelayer as CallbackDelayer
from vehicle_systems.tankStructure import TankPartIndexes as TankPartIndexes
from components_base.component_descriptor import ComponentDescriptorTyped as ComponentDescriptorTyped
from battleground.component_loading import loadComponentSystem as loadComponentSystem, Loader as Loader
from battleground.components import SequenceComponent as SequenceComponent, AvatarRelatedComponent as AvatarRelatedComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
_logger: Any

class BerserkerEffectComponent(AvatarRelatedComponent):
    __sessionProvider: Any
    __dynObjectsCache: Any
    __APPEARANCE_COMPONENT_NAME = 'berserker'
    __loadingEffects: Any
    __activeEffectsTime: Any
    def __init__(self, componentSystem):
        ...
    def deactivate(self):
        ...
    def _initialize(self):
        ...
    def __onEquipmentComponentUpdated(self, _, vehicleID, data):
        ...
    def __addEffect(self, vehicleId, endTime):
        ...
    def __onEffectLoaded(self, effObject):
        ...
    def __destroyEffect(self, vehicleId):
        ...
    def __getLoaders(self):
        ...
    def __onVehicleUpgradeStarted(self, vehicleId):
        ...
    def __onVehicleUpgradeFinished(self, vehicleId):
        ...

class _VehicleNodeEffect(SequenceComponent):
    _TANK_PART_INDEX = None
    __node: Any
    __fakeModel: Any
    __vehicleId: Any
    def __init__(self, sequenceAnimator):
        ...
    @property
    def finished(self):
        ...
    def setVehicleId(self, vId):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def _getModuleName(self, typeDescriptor):
        ...
    def __getTransform(self, vehicle):
        ...

class _VehicleHullEffect(_VehicleNodeEffect):
    _TANK_PART_INDEX = TankPartIndexes.HULL
    def _getModuleName(self, typeDescriptor):
        ...

class _VehicleTurretEffect(_VehicleNodeEffect):
    _TANK_PART_INDEX = TankPartIndexes.TURRET
    def _getModuleName(self, typeDescriptor):
        ...

class _BerserkerEffectObject(ComponentController):
    turretEffectPlayer: Any
    hullEffectPlayer: Any
    __vehicleId: Any
    __doneCallback: Any
    __endTime: Any
    __callbackDelayer: Any
    def __init__(self, vehicleId, endTime, doneCallback):
        ...
    @property
    def vehicleId(self):
        ...
    @property
    def endTime(self):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def destroy(self):
        ...
    def tick(self):
        ...
    def __finish(self):
        ...

class _TransformationParser(object):
    __DEFAULT_SECTION = 'default'
    __vehicleTransformations: dict
    __dynObjectsCache: Any
    __sessionProvider: Any
    @classmethod
    def parse(cls):
        ...
    @classmethod
    def getTransform(cls, vehName, vehPartName, moduleName):
        ...

class BerserkerEffectObjectsSystem(CGF.System):
    Activate: Any
    Deactivate: Any
    Iterate: Any
    Reactions: Any
    def update(self):
        ...
