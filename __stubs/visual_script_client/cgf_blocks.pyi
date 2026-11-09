# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/cgf_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import weakref as weakref
import BigWorld as BigWorld
from constants import IS_VS_EDITOR as IS_VS_EDITOR, ROCKET_ACCELERATION_STATE as ROCKET_ACCELERATION_STATE, UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from debug_utils import LOG_WARNING as LOG_WARNING
from visual_script.block import Block as Block
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.misc import ASPECT as ASPECT, errorVScript as errorVScript
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.contexts.cgf_context import GameObjectWrapper as GameObjectWrapper
from visual_script.cgf_blocks import CGFMeta as CGFMeta
from gui.battle_control.controllers.vehicle_passenger import IVehiclePassengerController as IVehiclePassengerController
Vehicle: Any
CGF: Any
tankStructure: Any
RAC: Any
SimulatedVehicle: Any
cgf_helpers: Any
GenericComponents: Any
_logger: Any

class VehiclePassengerInfoWatcher(object):
    ...

class CGFClientMeta(CGFMeta):
    @classmethod
    def blockAspects(cls):
        ...

class HierarchySingletonMixin(object):
    _hierarchySingleton: Any
    def __init__(self):
        ...
    def _setHierarchySingleton(self, go):
        ...

class GetVehicleAppearanceGameObject(Block, CGFClientMeta, HierarchySingletonMixin):
    _object: Any
    _appObject: Any
    def __init__(self, *args, **kwargs):
        ...
    def validate(self):
        ...
    def onStartScript(self):
        ...
    def _exec(self):
        ...

class GetVehicleGameObject(Block, CGFClientMeta, HierarchySingletonMixin):
    _object: Any
    _vehicleObject: Any
    def __init__(self, *args, **kwargs):
        ...
    def validate(self):
        ...
    def onStartScript(self):
        ...
    def _exec(self):
        ...

class RocketAcceleratorEvents(Block, CGFClientMeta):
    _activate: Any
    _deactivate: Any
    _object: Any
    _activateOut: Any
    _deactivateOut: Any
    _failure: Any
    _deploying: Any
    _preparing: Any
    _empty: Any
    _ready: Any
    _active: Any
    _disabled: Any
    _tryActivate: Any
    _duration: Any
    __switcher: Any
    __controllerLink: Any
    def __init__(self, *args, **kwargs):
        ...
    def __activate(self):
        ...
    def __deactivate(self):
        ...
    def __onStateChange(self, status, _):
        ...
    def __onTryActivate(self):
        ...
    def __onWrongState(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class RocketAcceleratorSettings(Block, CGFClientMeta):
    _activate: Any
    _object: Any
    _out: Any
    _failure: Any
    _isPlayer: Any
    def __init__(self, *args, **kwargs):
        ...
    def __execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnVehiclePassengerInfo(Block, CGFClientMeta, VehiclePassengerInfoWatcher):
    _vehicleID: Any
    _subscribe: Any
    _unsubscribe: Any
    _object: Any
    _subscribeOut: Any
    _unsubscribeOut: Any
    _onVehicleInfoUpdating: Any
    _onVehicleInfoUpdate: Any
    _isPlayerVehicle: Any
    _isCurrentVehicle: Any
    _isCurrentVehicleFPV: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def __subscribe(self):
        ...
    def __subscribeVehicle(self, vehicle):
        ...
    def __unsubscribe(self):
        ...
    def __onVehiclePassengerUpdating(self, _):
        ...
    def __onVehiclePassengerUpdate(self, _):
        ...
    # decorador original: @hasVehiclePassengerCtrl(...)
    def __updateVehicleInfoByPassenger(self, passengerCtrl=None):
        ...

def hasVehiclePassengerCtrl(*_, **__):
    ...
def _extractRACComponent(gameObjectLink):
    ...
