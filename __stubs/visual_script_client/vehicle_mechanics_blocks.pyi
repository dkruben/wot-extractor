# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/visual_script_client/vehicle_mechanics_blocks.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from constants import AUTORELOADER_SURGE_RESTRICTION as AUTORELOADER_SURGE_RESTRICTION, BUSTLE_FEED_SWITCH_ACCESS as BUSTLE_FEED_SWITCH_ACCESS, OVERHEAT_GAIN_STATE as OVERHEAT_GAIN_STATE, SIGHT_POINTER_COMMON_CONSTANTS as SIGHT_POINTER_COMMON_CONSTANTS, TARGET_DESIGNATOR_STATE as TARGET_DESIGNATOR_STATE
from events_handler import eventHandler as eventHandler
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.generic_mechanics.wheeled_dash import IWheeledDashListenerLogic as IWheeledDashListenerLogic
from vehicles.mechanics.mechanic_commands import IMechanicCommandsListenerLogic as IMechanicCommandsListenerLogic
from vehicles.mechanics.mechanic_constants import VEHICLE_MECHANIC_USED_COMMANDS as VEHICLE_MECHANIC_USED_COMMANDS
from visual_script.block import Block as Block
from visual_script.dependency import dependencyImporter as dependencyImporter
from visual_script.misc import ASPECT as ASPECT
from visual_script.slot_types import SLOT_TYPE as SLOT_TYPE
from visual_script.vehicle_mechanics_blocks import AcceleratorStatusEnum as AcceleratorStatusEnum, BustleFeedStateEnum as BustleFeedStateEnum, ConcentrationModeStateEnum as ConcentrationModeStateEnum, HeatingZonesGunEnum as HeatingZonesGunEnum, LowChargeShotStateEnum as LowChargeShotStateEnum, OverheatGainStateEnum as OverheatGainStateEnum, OverheatGunEnum as OverheatGunEnum, PhasedMechanicStateEnum as PhasedMechanicStateEnum, PowerModeStateEnum as PowerModeStateEnum, PropellantGunEnum as PropellantGunEnum, RechargeableNitroStateEnum as RechargeableNitroStateEnum, SecondaryGunStateEnum as SecondaryGunStateEnum, SightPointerStateEnum as SightPointerStateEnum, StationaryReloadEnum as StationaryReloadEnum, StationaryReloadLockEnum as StationaryReloadLockEnum, TargetDesignatorStateEnum as TargetDesignatorStateEnum, TemperatureGunEnum as TemperatureGunEnum, VehicleMechanicsMeta as VehicleMechanicsMeta, VehicleSiegeStateEnum as VehicleSiegeStateEnum, WheeledDashDirectionEnum as WheeledDashDirectionEnum, ShellParamsSwitcherGunEnum as ShellParamsSwitcherGunEnum, AutoreloaderSurgeStateEnum as AutoreloaderSurgeStateEnum
from visual_script_client.vehicle_mechanics_common import VehicleMechanicEventsBlock as VehicleMechanicEventsBlock, VehicleMechanicLifeCycleEventsBlock as VehicleMechanicLifeCycleEventsBlock, VehicleMechanicStateEventsBlock as VehicleMechanicStateEventsBlock, VehicleSelectableMechanicEventsBlock as VehicleSelectableMechanicEventsBlock
from typing import Any as Any, List as List
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from AccuracyStacksController import AccuracyStacksState as AccuracyStacksState
from BattleFuryController import BattleFuryState as BattleFuryState
from ChargeShotComponent import ChargeShotState as ChargeShotState
from ConcentrationModeComponent import ConcentrationModeState as ConcentrationModeState
from vehicles.mechanics.generic_mechanics.bustle_feed import BustleFeedState as BustleFeedState
from items.components.shared_components import ChargeShotParams as ChargeShotParams
from LowChargeShotController import LowChargeShotMechanicState as LowChargeShotMechanicState
from OverheatStacksController import OverheatStacksState as OverheatStacksState
from PillboxSiegeComponent import PillboxSiegeModeState as PillboxSiegeModeState
from PowerModeController import PowerModeState as PowerModeState
from RechargeableNitroController import RechargeableNitroState as RechargeableNitroState
from SightPointerComponent import SightPointerState as SightPointerState
from StagedJetBoostersController import StagedJetBoostersState as StagedJetBoostersState
from StanceDanceController import StanceDanceState as StanceDanceState
from StationaryReloadController import StationaryReloadModeState as StationaryReloadModeState
from SupportWeaponComponent import SupportWeaponState as SupportWeaponState
from TargetDesignatorController import TargetDesignatorState as TargetDesignatorState
from TemperatureGunController import TemperatureGunMechanicState as TemperatureGunMechanicState
from vehicles.mechanics.gun_mechanics.propellant_gun import IPropellantGunMechanicState as IPropellantGunMechanicState
from vehicles.mechanics.gun_mechanics.temperature.heating_zones_gun import IHeatingZonesGunMechanicState as IHeatingZonesGunMechanicState
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import IOverheatGunComponentParams as IOverheatGunComponentParams, IOverheatGunMechanicState as IOverheatGunMechanicState
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from WheeledDashController import WheeledDashState as WheeledDashState
from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher import AuxiliaryRocketLauncherState as AuxiliaryRocketLauncherState
from vehicles.mechanics.generic_mechanics.spec_boost_mode import SpecBoostModeMechanicState as SpecBoostModeMechanicState
from ShellCalibrationController import ShellCalibrationModeState as ShellCalibrationModeState
from AutoreloaderSurgeController import AutoreloaderSurgeState as AutoreloaderSurgeState
cgf_helpers: _Any
_logger: _Any
_AUTORELOADER_SURGE_RESTRICTION_TO_ERROR_KEY: dict

class ServerTime(Block):
    _currentTimestamp: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def blockAspects(cls):
        ...
    @classmethod
    def blockIcon(cls):
        ...
    @classmethod
    def blockCategory(cls):
        ...
    def _execValue(self):
        ...

class OnVehicleMechanicCommand(VehicleSelectableMechanicEventsBlock, IMechanicCommandsListenerLogic):
    _EVENTS_NAME = 'commands'
    _commands: _Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicCommand(self, command):
        ...
    @classmethod
    def _getInitParamMechanics(cls):
        ...

class OnConcentrationModeState(VehicleMechanicStateEventsBlock):
    _state: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnPowerModeState(VehicleMechanicStateEventsBlock):
    _state: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def _onStateObservation(self, state):
        ...

class OnPillboxSiegeModeState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _nextState: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, _, newState):
        ...

class OnRechargeableNitroState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _isCharged: _Any
    _isEmpty: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def __forwardStateToVSE(self, state):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def _onStateObservation(self, state):
        ...

class OnBattleFuryState(VehicleMechanicStateEventsBlock):
    _prevLevelSlot: _Any
    _levelSlot: _Any
    _maxLevel: _Any
    _prevEndTimeSlot: _Any
    _endTimeSlot: _Any
    _prevLevel: _Any
    _level: _Any
    _prevEndTime: _Any
    _endTime: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def __recacheState(self, newState):
        ...
    def __setSlots(self):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnOverheatStacksState(VehicleMechanicStateEventsBlock):
    _prevGainState: _Any
    _gainState: _Any
    _prevLevel: _Any
    _level: _Any
    _maxLevel: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnAccuracyStacksState(VehicleMechanicStateEventsBlock):
    _prevIsGainingActive: _Any
    _isGainingActive: _Any
    _prevLevel: _Any
    _level: _Any
    _maxLevel: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnSupportWeaponState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _timeLeft: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnStanceDanceState(VehicleMechanicStateEventsBlock):
    _isFightState: _Any
    _isTurboState: _Any
    _isActiveFightState: _Any
    _isActiveTurboState: _Any
    _isEngineDeadState: _Any
    _isSwitchingState: _Any
    _fightEnergyRatio: _Any
    _turboEnergyRatio: _Any
    _isEnoughEnergyToActivate: _Any
    _prevIsFightState: _Any
    _prevIsTurboState: _Any
    _prevIsActiveFightState: _Any
    _prevIsActiveTurboState: _Any
    _prevIsEngineDeadState: _Any
    _prevIsSwitchingState: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def __updateCurrentState(self, state):
        ...
    def __updatePrevState(self, state):
        ...

class OnChargeShotState(VehicleMechanicStateEventsBlock):
    _level: _Any
    _isCharging: _Any
    _isShotBlock: _Any
    _canStart: _Any
    _isGunDestroyed: _Any
    _prevLevel: _Any
    _prevIsCharging: _Any
    _prevIsShotBlock: _Any
    _prevIsGunDestroyed: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def __updateStateParams(self, currentState):
        ...

class OnChargeShotParams(VehicleMechanicLifeCycleEventsBlock):
    _maxLevel: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    # decorador original: @eventHandler
    def _onComponentParamsCollected(self, params):
        ...

class OnTargetDesignatorState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _prevState: _Any
    _endTime: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def __updateState(self, state):
        ...

class OnStationaryReloadState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _lockState: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class GetTemperatureTimeLeft(Block, VehicleMechanicsMeta):
    _in: _Any
    _out: _Any
    _object: _Any
    _targetTemp: _Any
    _cooldownTime: _Any
    def __init__(self, *args, **kwargs):
        ...
    def _execute(self):
        ...
    @classmethod
    def blockAspects(cls):
        ...

class OnTemperatureGunState(VehicleMechanicStateEventsBlock):
    _state: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnOverheatGunState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _prevState: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnOverheatGunParams(VehicleMechanicLifeCycleEventsBlock):
    _overheatOffThreshold: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    # decorador original: @eventHandler
    def _onComponentParamsCollected(self, params):
        ...

class OnHeatingZonesGunState(VehicleMechanicStateEventsBlock):
    _state: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnStagedJetBoostersState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _acceleratorStatus: _Any
    _duration: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def _onStateObservation(self, state):
        ...
    def __forwardStateToVSE(self, state):
        ...

class OnLowChargeShotState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _duration: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def _onStateObservation(self, state):
        ...
    def __forwardStateToVSE(self, state):
        ...

class OnPropellantGunState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _isOvercharge: _Any
    _isAvailable: _Any
    _isLastStage: _Any
    _isLastChargeStage: _Any
    _isMaxOverCharged: _Any
    _isMaxCharged: _Any
    _timeLeft: _Any
    _isUsableShell: _Any
    __prevState: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    def _onStateObservation(self, state):
        ...

class OnWheeledDashState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _duration: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, _):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, _, newState):
        ...
    def _onStateObservation(self, state):
        ...
    def __forwardStateToVSE(self, state):
        ...

class OnWheeledDashImpulse(VehicleMechanicEventsBlock, IWheeledDashListenerLogic):
    _onImpulseStarted: _Any
    _direction: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, _):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentReleasing(self, component):
        ...
    # decorador original: @eventHandler
    def onImpulseStarted(self, direction):
        ...

class OnAuxiliaryRocketLauncherState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _duration: _Any
    _isInAimingMode: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, _):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, _, newState):
        ...
    def _onStateObservation(self, state):
        ...
    def __forwardStateToVSE(self, state):
        ...

class OnShellParamsSwitcherGunState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _isBroken: _Any
    _isNoAmmo: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def __setState(self, state):
        ...

class OnShellCalibrationState(VehicleMechanicStateEventsBlock):
    _isPenBonusActive: _Any
    _isNonPenBonusActive: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStateTransition(self, prevState, newState):
        ...

class OnAutoreloaderSurgeState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _hasRestrictions: _Any
    _chargeIntervalEnd: _Any
    _restrictionErrorKey: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    # decorador original: @eventHandler
    def onMechanicComponentCatching(self, component):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def _onStateObservation(self, state):
        ...
    def __forwardStateToVSE(self, state):
        ...

class OnBustleFeedState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _prevState: _Any
    _canSwitch: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
    def __forwardStateToVSE(self, state):
        ...

class OnSightPointerState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _hasVehicles: _Any
    _stage: _Any
    _startTime: _Any
    _minActiveTime: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def __forwardStateToVSE(self, state):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, _, newState):
        ...

class OnCombatThrottleState(VehicleMechanicStateEventsBlock):
    _state: _Any
    _prevState: _Any
    def __init__(self, *args, **kwargs):
        ...
    @classmethod
    def _getVehicleMechanicKey(cls, initParams):
        ...
    def _onStatePrepared(self, state):
        ...
    def _onStateObservation(self, state):
        ...
    def _onStateTransition(self, prevState, newState):
        ...
