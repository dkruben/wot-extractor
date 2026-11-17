# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/player_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
import BigWorld as BigWorld
from aih_constants import CTRL_MODES as CTRL_MODES
from constants import DEFAULT_GUN_INSTALLATION_INDEX as DEFAULT_GUN_INSTALLATION_INDEX, EQUIPMENT_STAGES as EQUIPMENT_STAGES
from items import vehicles as vehicles
from visual_script import ASPECT as ASPECT
from visual_script.ability_common import Stage as Stage
from visual_script.block import Meta as Meta, Block as Block, InitParam as InitParam, buildStrKeysValue as buildStrKeysValue
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import errorVScript as errorVScript, EDITOR_TYPE as EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE, arrayOf as arrayOf
from visual_script.type import VScriptEnum as VScriptEnum
from visual_script.tunable_event_block import TunableEventBlock as TunableEventBlock
from visual_script_client.vehicle_common import TunablePlayerVehicleEventBlock as TunablePlayerVehicleEventBlock, getPartState as getPartState, getPartNames as getPartNames, getPartName as getPartName, TriggerListener as TriggerListener
from Vehicle import StunInfo as StunInfo
helpers: Any
TriggersManager: Any
gun_marker_ctrl: Any
equipment_ctrl: Any
Avatar: Any

class PlayerMeta(Meta):
    @classmethod
    def blockColor(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    @property
    def _avatar(self):
        ...

class PlayerEventMeta(PlayerMeta):
    @classmethod
    def blockIcon(cls):
        ...

class GetPlayerVehicleGun(Block, PlayerMeta):
    _gunPosition: Any
    _gunDirection: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getGunPosition(self):
        ...
    def _getGunDirection(self):
        ...

class GetPlayerGunMarkerInfo(Block, PlayerMeta):
    _pos: Any
    _dir: Any
    _size: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def _markerInfo(self):
        ...
    def _getPosition(self):
        ...
    def _getDirection(self):
        ...
    def _getSize(self):
        ...

class OnPlayerSnipeMode(TunableEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES: list
    _index: Any
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def onTriggerActivated(self, params):
        ...
    def onTriggerDeactivated(self, params):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnEnter(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnExit(self):
        ...

class OnPlayerSPGMode(TunableEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES: list
    _index: Any
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def onTriggerActivated(self, params):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnEnterTopDown(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnEnterTrajectory(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnExit(self):
        ...

class OnPlayerControlModeChange(TunableEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES: list
    __CTRL_MODE_ANY = 'Any mode'
    _controlMode: Any
    _previousMode: Any
    _currentMode: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def initParams(cls):
        ...
    def captionText(self):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def onTriggerActivated(self, params):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnExit(self, previousMode, currentMode):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnEnter(self, previousMode, currentMode):
        ...
    def __setOutputValues(self, previousMode, currentMode):
        ...

class IsControlModeActive(Block, PlayerEventMeta):
    _controlMode: Any
    _active: Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    def __execute(self):
        ...

class PlayerControlMode(VScriptEnum):
    @classmethod
    def slotType(cls):
        ...
    @classmethod
    def vs_enum(cls):
        ...
    @classmethod
    def nameToIndex(cls, ctrlModeName):
        ...
    @classmethod
    def _vs_collectEnumEntries(cls):
        ...
    @classmethod
    def vs_aspects(cls):
        ...

class OnGunMarkerPenetrationStateChanged(TunableEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _state: Any
    _oldResult: Any
    def __init__(self, *args, **kwargs):
        ...
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def _onGunMarkerStateChanged(self, _, gunMarkerState, __):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self, result):
        ...

class GetPlayerVehicleDeviceState(Block, PlayerMeta):
    _device: Any
    _state: Any
    _hasDevice: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execState(self):
        ...
    def _execHasDevice(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class GetPlayerVehicleTankmanState(Block, PlayerMeta):
    _tankman: Any
    _state: Any
    _hasTankman: Any
    def __init__(self, *args, **kwargs):
        ...
    def _execState(self):
        ...
    def _execHasTankman(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnPlayerVehicleDiscreteShoot(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    def onPlayerDiscreteShoot(self, gunInstallationIndex):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self):
        ...

class OnPlayerShotMissed(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    def onPlayerShotMissed(self, gunInstallationIndex):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self):
        ...

class OnPlayerShotHit(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _target: Any
    _flags: Any
    def __init__(self, *args, **kwargs):
        ...
    def onPlayerShotHit(self, target, flags, gunInstallationIndex):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self, target, flags):
        ...

class OnPlayerAutoAim(TunablePlayerVehicleEventBlock, PlayerEventMeta, TriggerListener):
    _EVENT_SLOT_NAMES: list
    _index: Any
    def onStartScript(self):
        ...
    def onFinishScript(self):
        ...
    def onTriggerActivated(self, params):
        ...
    def onTriggerDeactivated(self, params):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnEnter(self):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOnExit(self):
        ...

class OnPlayerMoveVehicle(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _forward: Any
    _backward: Any
    _left: Any
    _right: Any
    _cc25: Any
    _cc50: Any
    _break: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def onPlayerMove(self, moveCommands):
        ...
    @staticmethod
    def _processMoveCommand(moveCommands, commandToCheck, slotToSet):
        ...

class OnPlayerVehicleDetectEnemy(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _target: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    def onPlayerDetectEnemy(self, new, lost):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self, vehicle):
        ...

class OnPlayerVehicleFireEvent(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _index: Any
    def onPlayerVehicleFireEvent(self, isStart):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self):
        ...

class OnPlayerVehicleContinuousBurstStart(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    def onPlayerContinuousBurstStart(self, gunInstallationIndex):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self):
        ...

class OnPlayerVehicleContinuousBurstStop(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    def onPlayerContinuousBurstStop(self, gunInstallationIndex):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self):
        ...

class OnPlayerVehicleTankmanEvent(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _tankman: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    def onPlayerVehicleTankmanEvent(self, tankmanName, isHit):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self, tankman):
        ...

class OnPlayerVehicleDeviceCrit(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _device: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    def onPlayerVehicleDeviceEvent(self, deviceName, isCritical, isHit):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self, device):
        ...

class OnPlayerVehicleAreaTrigger(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _trigger: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    def onPlayerEnterTrigger(self, trigger, enter):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self):
        ...
    def validate(self):
        ...

class OnShowTracer(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _attacker: Any
    _isRicochet: Any
    _startPoint: Any
    _direction: Any
    _velocity: Any
    _gravity: Any
    _maxDist: Any
    def __init__(self, *args, **kwargs):
        ...
    def onShowTracer(self, attacker, isRicochet, startPoint, velocity, gravity, maxShotDist, gunInstallationIndex):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self, attacker, isRicochet, startPoint, velocity, gravity, maxShotDist):
        ...

class GetPlayerGunDispersionAngles(Block, PlayerMeta):
    _current: Any
    _target: Any
    _ideal: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getCurrentDispersions(self):
        ...
    def _getIdealDispersion(self):
        ...

class GetPlayerEquipments(Block, PlayerMeta):
    _equipments: Any
    def __init__(self, *args, **kwargs):
        ...
    def _getEquipments(self):
        ...

class GetPlayerEquipmentState(Block, PlayerMeta):
    _equipmentName: Any
    _equipped: Any
    _availableToUse: Any
    _canActivate: Any
    _isReady: Any
    _stage: Any
    _prevStage: Any
    _remainingTime: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def _equipment(self):
        ...
    def _isEquipped(self):
        ...
    def _canBeActivated(self):
        ...
    def _isAvailableToUse(self):
        ...
    def _getStage(self):
        ...
    def _getPrevStage(self):
        ...
    def _getTotalTime(self):
        ...
    def _getIsReady(self):
        ...

class OnPlayerVehicleStun(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _stunDuration: Any
    _lastStartTime: Any
    _lastDuration: Any
    _index: Any
    def __init__(self, *args, **kwargs):
        ...
    def _reset(self):
        ...
    def onStunInfoUpdated(self, stunInfo):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def _callOutput(self):
        ...

class OnVehicleSixthSenseActivated(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    # decorador original: @TunableEventBlock.eventProcessor
    def onSixthSenceActivated(self):
        ...

class OnPlayerUsedAOEEquipment(TunablePlayerVehicleEventBlock, PlayerEventMeta):
    _EVENT_SLOT_NAMES: list
    _name: Any
    _position: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @TunableEventBlock.eventProcessor
    def onPlayerUsedAoEEquipment(self, name, position):
        ...

class GetPlayerShellsState(Block, PlayerMeta):
    _shellsLeft: Any
    _shellsLoaded: Any
    _loadPercent: Any
    def __init__(self, *args, **kwargs):
        ...
    def _shells(self):
        ...
    def _curLoadPercentLeft(self):
        ...

def isMainGunInstallation(gunInstallationIndex):
    ...
