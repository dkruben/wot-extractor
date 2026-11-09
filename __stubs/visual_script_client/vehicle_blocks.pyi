# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/vehicle_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import random as random
import weakref as weakref
import BigWorld as BigWorld
from constants import IS_VS_EDITOR as IS_VS_EDITOR, VEHICLE_CLASSES as VEHICLE_CLASSES, OVERTURN_WARNING_LEVEL as OVERTURN_WARNING_LEVEL, DROWN_WARNING_LEVEL as DROWN_WARNING_LEVEL
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from visual_script.block import Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import ASPECT as ASPECT, EDITOR_TYPE as EDITOR_TYPE, errorVScript as errorVScript
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.tunable_event_block import TunableEventBlock as TunableEventBlock
from visual_script.type import VScriptEnum as VScriptEnum
from visual_script.vehicle_blocks import VehicleMeta as VehicleMeta
from visual_script.vehicle_blocks_bases import NoCrewCriticalBase as NoCrewCriticalBase, OptionalDevicesBase as OptionalDevicesBase, VehicleClassBase as VehicleClassBase, GunTypeInfoBase as GunTypeInfoBase, VehicleForwardSpeedBase as VehicleForwardSpeedBase, VehicleCooldownEquipmentBase as VehicleCooldownEquipmentBase, VehicleClipFullAndReadyBase as VehicleClipFullAndReadyBase, GetTankOptDevicesHPModBase as GetTankOptDevicesHPModBase, IsInHangarBase as IsInHangarBase, VehicleRadioDistanceBase as VehicleRadioDistanceBase, NoInnerDeviceDamagedBase as NoInnerDeviceDamagedBase
from helpers import dependency as dependency, isPlayerAccount as isPlayerAccount, isPlayerAvatar as isPlayerAvatar
from skeletons.gui.shared import IItemsCache as IItemsCache
from VehicleRespawnComponent import VehicleRespawnComponent as VehicleRespawnComponent
from typing import Optional as Optional
from Vehicle import Vehicle as Vehicle
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot
OwnVehicle: Any
EntitySync: Any

class OverturnWarningLevelEnum(VScriptEnum):
    @classmethod
    def slotType(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class DrownWarningLevelEnum(VScriptEnum):
    @classmethod
    def slotType(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class GetVehicleLabel(Block, VehicleMeta):
    _vehicle: Any
    _label: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getLabel(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnAnyVehicleDestroyed(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES: list
    _target: Any
    _attacker: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def __onVehicleKilled(self, targetID, attackerID, equipmentID, reason, numVehiclesAffected):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnAnyVehicleDamaged(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES: list
    _target: Any
    _attacker: Any
    _damage: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def __onDamageReceived(self, vehicleId, attackerId, damage):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class IsVehicleBurning(Block, VehicleMeta):
    _vehicle: Any
    _res: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class NoCrewCritical(NoCrewCriticalBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class NoInnerDeviceDamaged(NoInnerDeviceDamagedBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OptionalDevices(OptionalDevicesBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetTankOptDevicesHPMod(GetTankOptDevicesHPModBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class VehicleClass(VehicleClassBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GunTypeInfo(GunTypeInfoBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class VehicleForwardSpeed(VehicleForwardSpeedBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class VehicleCooldownEquipment(VehicleCooldownEquipmentBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class VehicleClipFullAndReady(VehicleClipFullAndReadyBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetNearestAliveVehicle(Block, VehicleMeta):
    _settingTypes: list
    _settingType: Any
    _position: Any
    _vehicle: Any
    @classmethod
    def initParams(cls):
        ...
    def __init__(self, *args, **kwargs):
        ...
    def __checkVehicle(self, vehicle):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetAnyVehicle(Block, VehicleMeta):
    _settingTypes: list
    _settingType: Any
    _vehicle: Any
    @classmethod
    def initParams(cls):
        ...
    def __init__(self, *args, **kwargs):
        ...
    def __checkVehicle(self, vehicle):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GameObjectToVehicle(Block, VehicleMeta):
    _go: Any
    _vehicle: Any
    def __init__(self, *args, **kwargs):
        ...
    def _exec(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class IsInHangar(IsInHangarBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class VehicleRadioDistance(VehicleRadioDistanceBase):
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetVehicleTier(Block):
    _vehicle: Any
    _outSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnAnyVehicleRespawned(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES: list
    _vehicle: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _vehicleRespawnHandler(self, vehicle):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class VehicleMaxSpeed(Block, VehicleMeta):
    _vehicle: Any
    _speed: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnVehicleCollided(Block, VehicleMeta):
    _out: Any
    _vehicle: Any
    _velocity: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onVehicleCollided(self, vehicleId, velocity):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnVehicleShot(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES: list
    _vehicle: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def __onVehicleShot(self, vehicleId):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnVehicleHit(TunableEventBlock, VehicleMeta):
    _EVENT_SLOT_NAMES: list
    _vehicle: Any
    _withDamage: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def __onVehicleHit(self, vehicleId, damage):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetVehicleOverturnLevel(Block, VehicleMeta):
    _vehicleGO: Any
    _overturnLevel: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getData(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetVehicleDrownLevel(Block, VehicleMeta):
    _vehicleGO: Any
    _drownLevel: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getData(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnDiscreteShotDone(Block, VehicleMeta):
    _subscribe: Any
    _unsubscribe: Any
    _vehicle: Any
    _onDiscreteShotDoneSlot: Any
    def __init__(self, *args, **kwargs):
        ...
    def __subscribe(self):
        ...
    def __unsubscribe(self):
        ...
    def __onDiscreteShotDone(self, gunInstallationSlot):
        ...
    @classmethod
    def blockAspects(cls):
        ...
