# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/arena_component_system/arena_equipment_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from functools import partial as partial
from future.utils import viewitems as viewitems, viewvalues as viewvalues
import logging as logging
import BigWorld as BigWorld
import CGF as CGF
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from battle_royale.gui.constants import BattleRoyaleEquipments as BattleRoyaleEquipments
from arena_component_system.client_arena_component_system import ClientArenaComponent as ClientArenaComponent
from constants import ARENA_SYNC_OBJECTS as ARENA_SYNC_OBJECTS, ARENA_GUI_TYPE as ARENA_GUI_TYPE
from debug_utils import LOG_ERROR_DEV as LOG_ERROR_DEV
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID
from gui.battle_control.matrix_factory import makeVehicleEntityMP as makeVehicleEntityMP
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import vehicles as vehicles
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache as IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from smoke_screen import SmokeScreen as SmokeScreen
from AffectComponent import RepairAffectComponent as RepairAffectComponent, TrapAffectComponent as TrapAffectComponent, FireCircleAffectComponent as FireCircleAffectComponent
_logger: Any
_EQUIPMENT_AFFECT_COMPONENTS: dict
InspireArgs: Any
HealPointArgs: Any

class EffectData(object):
    TimerTuple: Any
    __sessionProvider: Any
    vehicleID: Any
    startTime: Any
    endTime: Any
    visualSettings: Any
    inactivationStartTime: Any
    inactivationEndTime: Any
    radius: Any
    primary: Any
    senderKey: Any
    equipmentID: Any
    inactivationSource: Any
    __timerTuple: Any
    class EFFECT_PERIOD(CONST_CONTAINER):
        EXPOSED = 0
        INACTIVATION = 1
        OVER = 2
    def __init__(self, vehicleID, startTime, endTime, visualSettings, inactivationStartTime=None, inactivationEndTime=None, primary=True, radius=None, senderKey=None, equipmentID=None, inactivationSource=False):
        ...
    def updateTerrainCircle(self):
        ...
    @property
    def isActive(self):
        ...
    def setNextCallback(self, func):
        ...
    def cancelCallback(self):
        ...
    def destroy(self):
        ...
    def getNextPeriodAndStartTime(self, currentTime, currentPeriod=None):
        ...
    def __invokeCallback(self, func, period):
        ...

class InspireArgsAdapter(InspireArgs):
    def __new__(cls, isSourceVehicle, isInactivation, endTime, duration, primary, _, equipmentID):
        ...

class HealPointArgsAdapter(HealPointArgs):
    def __new__(cls, isSourceVehicle, isInactivation, endTime, duration, _, senderKey, *__):
        ...

class Effect(object):
    name: Any
    args: Any
    vehicleViewState: Any
    feedbackEventID: Any
    visualSettings: Any
    exposedVehicles: Any
    providingVehicles: Any
    def __init__(self, name, args, vehicleViewState, feedbackEventID, visualSettings, exposedVehicles=None, providingVehicles=None):
        ...
    def destroy(self):
        ...

class ArenaEquipmentComponent(ClientArenaComponent, CallbackDelayer):
    sessionProvider: Any
    __dynamicObjectsCache: Any
    __smokeScreen: Any
    __healingEffect: Any
    __inspiringEffect: Any
    __repairPointEffect: Any
    def __init__(self, componentSystem):
        ...
    def activate(self):
        ...
    def deactivate(self):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __removeEffect(self, vehicleId, effect):
        ...
    def __updateExposedToEffect(self, vehicleID, senderKey, startTime, endTime, inactivationStartTime, inactivationEndTime, primary, equipmentID, effect, isInfluenceZone, inactivationSource):
        ...
    def __checkAffectComponent(self, vehicleID, affectComponentType, isInfluenceZone):
        ...
    def _updateEffectSource(self, vehicleID, startTime, endTime, inactivationDelay, effectSourceRadius, effect, equipmentID=None):
        ...
    def removeInspire(self, vehicleID):
        ...
    def removeHealPoint(self, vehicleID):
        ...
    def removeRepairPoint(self, vehicleID):
        ...
    def updateInspired(self, vehicleID, startTime, endTime, inactivationStartTime, inactivationEndTime, primary, equipmentID, inactivationSource):
        ...
    def updateHealing(self, vehicleID, senderKey, startTime, endTime, inactivationStartTime, inactivationEndTime):
        ...
    def updateHealOverTime(self, vehicleID, senderKey, startTime, endTime, inactivationStartTime, inactivationEndTime, isInfluenceZone):
        ...
    def updateDebuff(self, vehicleID, equipmentID):
        ...
    def updateInspiringSource(self, vehicleID, startTime, endTime, inactivationDelay, inspireSourceRadius, equipmentID):
        ...
    def updateHealingSource(self, vehicleID, startTime, endTime, inactivationDelay, healingSourceRadius):
        ...
    def __evaluateExposedData(self, data, period, effect):
        ...
    def __evaluateEffectSourceData(self, data, period, effect):
        ...
    def __restartEffectData(self, effectData, effect, isSource=False, atPeriod=None):
        ...
    def __getMotor(self, vehicleId):
        ...
    def __onSmokeScreenUpdated(self, args):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onCameraChanged(self, ctrlMode, _=None):
        ...
    def __updateSmokePostEffect(self):
        ...
    @staticmethod
    def __doUpdateSmokePostEffect():
        ...
