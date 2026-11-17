# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicle_extras.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import logging as logging
from functools import partial as partial
import BattleReplay as BattleReplay
from future.utils import lrange as lrange, viewitems as viewitems, viewvalues as viewvalues
import AnimationSequence as AnimationSequence
import BigWorld as BigWorld
import Math as Math
import material_kinds as material_kinds
from GenericComponents import findSlot as findSlot
from constants import IS_EDITOR as IS_EDITOR, CollisionFlags as CollisionFlags, DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX, IS_UE_EDITOR as IS_UE_EDITOR
from cgf_events import shot_event as shot_event
from debug_utils import LOG_CODEPOINT_WARNING as LOG_CODEPOINT_WARNING, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import i18n as i18n
from helpers.EffectsList import EffectsListPlayer as EffectsListPlayer
from helpers.EntityExtra import EntityExtra as EntityExtra
from helpers.prefab_effects import resolveGunPrefabEffects as resolveGunPrefabEffects
from helpers.laser_sight_matrix_provider import LaserSightMatrixProvider as LaserSightMatrixProvider
from items import vehicles as vehicles
from items.components.component_constants import MAIN_TRACK_PAIR_IDX as MAIN_TRACK_PAIR_IDX
from vehicle_systems.shooting_helpers import processVehicleSingleShot as processVehicleSingleShot, processVehicleMultiShot as processVehicleMultiShot
from vehicle_systems.stricted_loading import makeCallbackWeak as makeCallbackWeak
from vehicle_systems.vehicle_composition import VehicleSlots as VehicleSlots
_logger: Any

class NoneExtra(EntityExtra):
    __slots__: tuple
    def _start(self, data, args):
        ...

class ShowShooting(EntityExtra):
    __slots__: tuple
    def _start(self, data, args):
        ...
    def _cleanup(self, data):
        ...
    def __doShot(self, data):
        ...
    def __onComplete(self, data):
        ...
    def __postVehicleShotEvent(self, vehicle, shellType):
        ...
    def __doRecoil(self, vehicle, gunModel):
        ...
    def _doGroundWaveEffect(self, vehicle, groundWaveEff, gunModel, gunNode=None):
        ...

class ShowShootingMultiGun(ShowShooting):
    _SHOT_ALL_GUNS = -1
    def _start(self, data, args):
        ...
    def _cleanup(self, data):
        ...
    def __doShot(self, data):
        ...
    def __doGunEffect(self, data, gunIndexes, isLastEffect):
        ...
    def __doRecoil(self, data):
        ...

class DamageMarker(EntityExtra):
    __slots__: tuple
    deviceUserString: Any
    sounds: Any
    def _readConfig(self, dataSection, containerName):
        ...
    def _getDeviceUserString(self, dataSection, containerName):
        ...
    def _getSounds(self, soundSection):
        ...
    @property
    def isTankman(self):
        ...

class TrackHealth(DamageMarker):
    __slots__: tuple
    __isLeft: Any
    _trackPairIndex: Any
    def _readConfig(self, dataSection, containerName):
        ...
    def _getDeviceUserString(self, dataSection, _):
        ...
    def _start(self, data, args):
        ...
    def _cleanup(self, data):
        ...

class TrackWithinTrackHealth(TrackHealth):
    def _getDeviceUserString(self, dataSection, _):
        ...

class TankmanHealth(DamageMarker):
    @property
    def isTankman(self):
        ...

class BlinkingLaserSight(EntityExtra):
    __slots__: tuple
    _SEQUENCE_NAMES: tuple
    _MAX_LASER_DISTANCE = 564
    _isEnabledBlinking: Any
    _shouldCollideTarget: Any
    _beamLength: Any
    _bindNode: Any
    _beamSeqs: Any
    def _readConfig(self, dataSection, containerName):
        ...
    def _newData(self, entity):
        ...
    def _start(self, data, args):
        ...
    def _update(self, data, args):
        ...
    def _cleanup(self, data):
        ...
    @staticmethod
    def __onSequenceLoaded(seqName, data, resourceRefs):
        ...
    @staticmethod
    def __stopAnimator(data):
        ...
    @staticmethod
    def __stopModel(data):
        ...

def reload():
    ...
def wheelHealths(name, index, containerName, dataSection, vehType):
    ...
