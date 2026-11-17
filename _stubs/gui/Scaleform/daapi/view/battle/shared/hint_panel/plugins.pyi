# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/hint_panel/plugins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from battle_royale.gui.battle_control.controllers.radar_ctrl import IRadarListener as IRadarListener
import CommandMapping as CommandMapping
from Event import EventsSubscriber as EventsSubscriber
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import TRAJECTORY_VIEW_HINT_SECTION as TRAJECTORY_VIEW_HINT_SECTION, PRE_BATTLE_HINT_SECTION as PRE_BATTLE_HINT_SECTION, QUEST_PROGRESS_HINT_SECTION as QUEST_PROGRESS_HINT_SECTION, HELP_SCREEN_HINT_SECTION as HELP_SCREEN_HINT_SECTION, SIEGE_HINT_SECTION as SIEGE_HINT_SECTION, WHEELED_MODE_HINT_SECTION as WHEELED_MODE_HINT_SECTION, HINTS_LEFT as HINTS_LEFT, NUM_BATTLES as NUM_BATTLES, LAST_DISPLAY_DAY as LAST_DISPLAY_DAY, IBC_HINT_SECTION as IBC_HINT_SECTION, DEV_MAPS_HINT_SECTION as DEV_MAPS_HINT_SECTION, RADAR_HINT_SECTION as RADAR_HINT_SECTION, TURBO_SHAFT_ENGINE_MODE_HINT_SECTION as TURBO_SHAFT_ENGINE_MODE_HINT_SECTION, PRE_BATTLE_ROLE_HINT_SECTION as PRE_BATTLE_ROLE_HINT_SECTION, COMMANDER_CAM_HINT_SECTION as COMMANDER_CAM_HINT_SECTION, ROCKET_ACCELERATION_MODE_HINT_SECTION as ROCKET_ACCELERATION_MODE_HINT_SECTION, RESERVES_HINT_SECTION as RESERVES_HINT_SECTION, MAPBOX_HINT_SECTION as MAPBOX_HINT_SECTION, TWIN_GUN_HINT_SECTION as TWIN_GUN_HINT_SECTION, PILLBOX_HINT_SECTION as PILLBOX_HINT_SECTION, RECHARGEABLE_NITRO_MODE_HINT_SECTION as RECHARGEABLE_NITRO_MODE_HINT_SECTION, TARGET_DESIGNATOR_MODE_HINT_SECTION as TARGET_DESIGNATOR_MODE_HINT_SECTION, STAGED_JET_BOOSTERS_MODE_HINT_SECTION as STAGED_JET_BOOSTERS_MODE_HINT_SECTION, WHEELED_DASH_MODE_HINT_SECTION as WHEELED_DASH_MODE_HINT_SECTION, SHELL_PARAMS_SWITCHER_HINT_SECTION as SHELL_PARAMS_SWITCHER_HINT_SECTION, BUSTLE_FEED_HINT_SECTION as BUSTLE_FEED_HINT_SECTION
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import VEHICLE_SIEGE_STATE as _SIEGE_STATE, ARENA_PERIOD as ARENA_PERIOD, ARENA_GUI_TYPE as ARENA_GUI_TYPE, ROLE_TYPE as ROLE_TYPE, ROCKET_ACCELERATION_STATE as ROCKET_ACCELERATION_STATE, RECHARGEABLE_NITRO_STATE as RECHARGEABLE_NITRO_STATE, TARGET_DESIGNATOR_STATE as TARGET_DESIGNATOR_STATE, PHASED_MECHANIC_STATE as PHASED_MECHANIC_STATE, BUSTLE_FEED_STATE as BUSTLE_FEED_STATE
from events_containers.common.containers import ContainersListener as ContainersListener
from debug_utils import LOG_DEBUG as LOG_DEBUG
from events_handler import eventHandler as eventHandler
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HelpHintContext as HelpHintContext
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.battle.shared.hint_panel.dyn_squad_hint_plugin import DynSquadHintPlugin as DynSquadHintPlugin
from gui.Scaleform.daapi.view.battle.shared.hint_panel.hint_panel_plugin import HintPanelPlugin as HintPanelPlugin, HintData as HintData, HintPriority as HintPriority
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent, ViewEventType as ViewEventType, LoadViewEvent as LoadViewEvent
from gui.shared.utils.key_mapping import getReadableKey as getReadableKey, getVirtualKey as getVirtualKey
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdatersCollection as ViewUpdatersCollection
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from items import makeIntCompactDescrByID as makeIntCompactDescrByID
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore, IBattleCommunicationsSettings as IBattleCommunicationsSettings
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.goodies import IBoostersStateProvider as IBoostersStateProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import hasVehicleDescrMechanic as hasVehicleDescrMechanic, getVehicleDescrMechanics as getVehicleDescrMechanics, getVehicleMechanicsComponents as getVehicleMechanicsComponents
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.goodies.booster_state_provider import BoosterStateProvider as BoosterStateProvider
from PillboxSiegeComponent import PillboxSiegeModeState as PillboxSiegeModeState
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
_logger: Any
_HINT_MIN_VEHICLE_LEVEL = 4
_HINT_TIMEOUT = 6
_HINT_COOLDOWN = 4
_TRAJECTORY_VIEW_HINT_POSITION: tuple
_TRAJECTORY_VIEW_HINT_CHECK_STATES: tuple
BEFORE_START_BATTLE_PERIODS: tuple

class PRBSettings(object):
    HELP_IDX = 0
    QUEST_IDX = 1
    HINT_DAY_COOLDOWN = 30
    HINT_BATTLES_COOLDOWN = 100

class TrajectoryViewHintPlugin(HintPanelPlugin):
    __slots__: tuple
    sessionProvider: Any
    _HINT_DAY_COOLDOWN = 30
    _HINT_BATTLES_COOLDOWN = 10
    __isHintShown: Any
    __isDestroyTimerDisplaying: Any
    __isDeathZoneTimerDisplaying: Any
    __isObserver: Any
    __settings: Any
    __wasDisplayed: Any
    __callbackDelayer: Any
    __isSuitableVehicle: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def updateMapping(self):
        ...
    def setPeriod(self, period):
        ...
    def __setup(self, crosshairCtrl, vehicleCtrl):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __onStrategicCameraChanged(self, _):
        ...
    def __onVehicleStateUpdated(self, stateID, stateValue):
        ...
    def __isThereAnyIndicators(self):
        ...
    def __addHint(self):
        ...
    def __removeHint(self):
        ...
    def __onHintTimeOut(self):
        ...
    def _getHint(self):
        ...

class SiegeIndicatorHintPlugin(HintPanelPlugin):
    sessionProvider: Any
    settingsCore: Any
    _HINT_DAY_COOLDOWN = 30
    _HINT_BATTLES_COOLDOWN = 10
    __isEnabled: Any
    __siegeState: Any
    __settings: Any
    __isHintShown: Any
    __isInPostmortem: Any
    __isObserver: Any
    _isInRecovery: Any
    _isInProgressCircle: Any
    _isUnderFire: Any
    __isWheeledTech: Any
    __hasTurboshaftEngine: Any
    __hasHydraulicChassis: Any
    __hasRocketAcceleration: Any
    __hasTwinGun: Any
    __hasStagedJetBoosters: Any
    __hasWheeledDash: Any
    __hasBustleFeed: Any
    __hasShellParamsSwitcher: Any
    __isSuitableVehicle: Any
    __period: Any
    __isInDisplayPeriod: Any
    __callbackDelayer: Any
    __startCounterUpdated: Any
    __rocketCmp: Any
    __nitroCmp: Any
    __stagedJetBoostersCmp: Any
    __wheeledDashCmp: Any
    __bustleFeedCmp: Any
    __hasRechargeableNitro: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def updateMapping(self):
        ...
    def setPeriod(self, period):
        ...
    def __onHintUsed(self):
        ...
    def __updateHint(self):
        ...
    def __checkVehicleSuitability(self, vTypeDesc, isPillboxVehicle):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __onTryRocketAccelerationActivate(self):
        ...
    def __onTryRechargeableNitroActivate(self, command):
        ...
    def __onTryStagedJetBoostersActivate(self, command):
        ...
    def __onTryWheeledDashActivate(self, command):
        ...
    def __onTryBustleFeedSwitch(self, command):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onPostMortemSwitched(self, *_):
        ...
    def __onRespawnBaseMoving(self):
        ...
    def __updateDestroyed(self, _):
        ...
    def __onHintTimeOut(self):
        ...
    def _getHint(self):
        ...
    def __areOtherIndicatorsShown(self):
        ...
    def __getSuitableSetting(self):
        ...

class RadarHintPlugin(HintPanelPlugin, CallbackDelayer, IRadarListener):
    _sessionProvider: Any
    _settingsCore: Any
    _HINT_DAY_COOLDOWN = 30
    _HINT_BATTLES_COOLDOWN = 10
    _TIME_AFTER_RADAR_COOLDOWN = 1
    __isEnabled: Any
    __settings: Any
    __isHintShown: Any
    __isInPostmortem: Any
    __isObserver: Any
    __period: Any
    __isInDisplayPeriod: Any
    _isInRecovery: Any
    _isInProgressCircle: Any
    _isUnderFire: Any
    __cbOnRadarCooldown: Any
    __radarInProgress: Any
    __es: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def stop(self):
        ...
    def updateMapping(self):
        ...
    def setPeriod(self, period):
        ...
    def radarActivated(self, _):
        ...
    def reset(self):
        ...
    def timeOutDone(self):
        ...
    def radarActivationFailed(self, code):
        ...
    def startTimeOut(self, timeLeft, duration):
        ...
    def _getHint(self):
        ...
    def __showHint(self):
        ...
    def __hideHint(self):
        ...
    def __updateHint(self):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onPostMortemSwitched(self, *_):
        ...
    def __onHintTimeOut(self):
        ...
    def __areOtherIndicatorsShown(self):
        ...
    def __clearRadarCooldown(self):
        ...

class PreBattleHintPlugin(HintPanelPlugin):
    __slots__: tuple
    sessionProvider: Any
    lobbyContext: Any
    __isActive: Any
    __hintInQueue: Any
    __callbackDelayer: Any
    __questHintSettings: Any
    __helpHintSettings: Any
    __battleComHintSettings: Any
    __reservesHintSettings: Any
    __isInDisplayPeriod: Any
    __haveReqLevel: Any
    __vehicleId: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def isActive(self):
        ...
    def setPeriod(self, period):
        ...
    def updateMapping(self):
        ...
    def _getHint(self):
        ...
    def _makeHintData(self, resourceRoot, priority, hintCtx=None):
        ...
    def _canDisplayCustomHelpHint(self):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __updateHintCounterOnStart(self, section, vehicle, setting):
        ...
    def __onHintTimeOut(self):
        ...
    def __hasVehicleHelpHint(self, vTypeDesc):
        ...
    def __canDisplayVehicleHelpHint(self, vTypeDesc):
        ...
    def __canDisplayBattleCommunicationHint(self):
        ...
    def __canDisplayPersonalReservesActivationHint(self):
        ...
    def __canDisplayQuestHint(self):
        ...
    def __onHintTimeCooldown(self, lastHint):
        ...
    def __displayHint(self, hintType):
        ...
    def __handleShowBtnHint(self, event):
        ...
    def __handleLoadView(self, event):
        ...
    def __handlePressQuestBtn(self, _):
        ...

class DeathCamHintPlugin(HintPanelPlugin):
    sessionProvider: Any
    spectatorCtrl: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def _getHint(self):
        ...
    def __showHint(self):
        ...
    def __handleDeathFreeCamState(self, vehicleID):
        ...
    def __hideHint(self):
        ...

class RoleHelpPlugin(HintPanelPlugin):
    __slots__: tuple
    _sessionProvider: Any
    _HINTS_COUNT = 1
    _BATTLES_COUNT = 3
    __isActive: Any
    __settings: Any
    __vehicleCD: Any
    __isShown: Any
    __isVisible: Any
    __isInDisplayPeriod: Any
    __callbackDelayer: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    @classmethod
    def isAvailableToShow(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def isActive(self):
        ...
    def setPeriod(self, period):
        ...
    def _getHint(self):
        ...
    @classmethod
    def isAvailableInSettings(cls, vehCD):
        ...
    @classmethod
    def __getIsObserver(cls):
        ...
    def __initSettings(self, vehicleId):
        ...
    def __showHint(self):
        ...
    @staticmethod
    def __handleRoleToggleEvent(isVisible):
        ...
    def __handleLoadView(self, event):
        ...
    def __handleBattleLoading(self, event):
        ...
    def __hide(self):
        ...

class CommanderCameraHintPlugin(HintPanelPlugin, CallbackDelayer):
    __slots__: tuple
    sessionProvider: Any
    lobbyContext: Any
    __hintData: Any
    __currPeriod: Any
    __settings: Any
    __canShow: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def setPeriod(self, period):
        ...
    def updateMapping(self):
        ...
    def _getHintDataByCMD(self, hint):
        ...
    def __handleShowBtnHint(self, event):
        ...
    def __hideHint(self):
        ...
    def __displayHint(self, hint):
        ...
    def __onHintShow(self, event):
        ...

class MapsTrainingHelpHintPlugin(PreBattleHintPlugin):
    @classmethod
    def isSuitable(cls):
        ...
    def _getHint(self):
        ...
    def _canDisplayCustomHelpHint(self):
        ...

class HelpPlugin(HintPanelPlugin):
    __slots__: tuple
    _sessionProvider: Any
    _HINT_TIMEOUT = 6
    __isActive: Any
    __settings: Any
    __isShown: Any
    __isVisible: Any
    __isInDisplayPeriod: Any
    __callbackDelayer: Any
    __settingKey: Any
    __settingSectionName: Any
    _localeRes: Any
    __hintPriority: Any
    __hintContext: Any
    def __init__(self, settingSectionName, settingKey, localeRes, hintPriority, hintContext, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def setPeriod(self, period):
        ...
    def _getHint(self):
        ...
    def __showHint(self):
        ...
    def __onHintShown(self, event):
        ...
    def __handleLoadView(self, event):
        ...
    def __onBattleLoading(self, event):
        ...
    def __hide(self):
        ...

class MapboxHelpPlugin(HelpPlugin):
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...

class DevMapsHintPlugin(HelpPlugin):
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...

class VehicleMechanicPlugin(HintPanelPlugin):
    __updatersCollection: Any
    def __init__(self, parentObj):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def fini(self):
        ...
    def _getViewUpdaters(self):
        ...

class PillboxHelpPlugin(VehicleMechanicPlugin, ContainersListener, IMechanicStatesListenerLogic):
    sessionProvider: Any
    settingsCore: Any
    _CMD = CommandMapping.CMD_CM_VEHICLE_SWITCH_AUTOROTATION
    _HINT_DAY_COOLDOWN = 30
    _HINT_BATTLES_COOLDOWN = 10
    __isPillboxOnShown: Any
    __isSiegeOffShown: Any
    __isPillboxOffShown: Any
    __isInPostmortem: Any
    __isObserver: Any
    __isInRecovery: Any
    __isInProgressCircle: Any
    __isUnderFire: Any
    __isDestroyed: Any
    __isInDisplayPeriod: Any
    __period: Any
    __isSuitableVehicle: Any
    __isActive: Any
    __isVisible: Any
    __settings: Any
    __siegeState: Any
    __startCounterUpdated: Any
    __callbackDelayer: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def setPeriod(self, period):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    def _getViewUpdaters(self):
        ...
    def _updateHint(self):
        ...
    def _show(self):
        ...
    def _hide(self):
        ...
    def _getHint(self):
        ...
    def __canShow(self):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onPostMortemSwitched(self, *_):
        ...
    def __onRespawnBaseMoving(self):
        ...

class SkillActivatedHintPlugin(HintPanelPlugin):
    sessionProvider: Any
    settingsCore: Any
    _HINT_DAY_COOLDOWN = 30
    _HINT_BATTLES_COOLDOWN = 10
    __isInPostmortem: Any
    __isObserver: Any
    _isInRecovery: Any
    _isInProgressCircle: Any
    _isUnderFire: Any
    __isInDisplayPeriod: Any
    __period: Any
    __isSuitableVehicle: Any
    __isEnabled: Any
    __isHintShown: Any
    __callbackDelayer: Any
    __startCounterUpdated: Any
    __subscribedVehicleID: Any
    __settings: Any
    __hasTargetDesignator: Any
    def __init__(self, parentObj):
        ...
    @classmethod
    def isSuitable(cls):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def updateMapping(self):
        ...
    def setPeriod(self, period):
        ...
    def __onHintUsed(self):
        ...
    def __updateHint(self):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    def __onTryTargetDesignatorActivate(self, command):
        ...
    def __getTargetDesignatorCmp(self):
        ...
    def __onVehicleStateUpdated(self, state, value):
        ...
    def __onPostMortemSwitched(self, *_):
        ...
    def __onRespawnBaseMoving(self):
        ...
    def __updateDestroyed(self, _):
        ...
    def __onHintTimeOut(self):
        ...
    def _getHint(self):
        ...
    def __areOtherIndicatorsShown(self):
        ...
    def __getSuitableSetting(self):
        ...

def createPlugins():
    ...
