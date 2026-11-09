# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/legacy_mechanics/dualgun_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from weakref import proxy as proxy
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from ReplayEvents import g_replayEvents as g_replayEvents
from Vehicle import StunInfo as StunInfo
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from constants import ARENA_PERIOD as ARENA_PERIOD
from constants import DUALGUN_CHARGER_STATUS as DUALGUN_CHARGER_STATUS
from constants import DUAL_GUN as DUAL_GUN
from constants import VEHICLE_MISC_STATUS as VEHICLE_MISC_STATUS
from debug_utils import LOG_WARNING as LOG_WARNING
from items.utils import getFirstReloadTime as getFirstReloadTime
from gui.Scaleform.daapi.view.meta.DualGunPanelMeta import DualGunPanelMeta as DualGunPanelMeta
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE, FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, DestroyTimerViewState as DestroyTimerViewState
from gui.battle_control.controllers.prebattle_setups_ctrl import IPrebattleSetupsListener as IPrebattleSetupsListener
from gui.Scaleform.daapi.view.battle.shared.legacy_mechanics.dualgun_sounds import DualGunSounds as DualGunSounds
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from helpers.time_utils import MS_IN_SECOND as MS_IN_SECOND
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from wotdecorators import noexceptReturn as noexceptReturn

class GunStatesUI(object):
    EMPTY = 1
    RELOADING = 2
    READY = 3

class DualGunConstants(object):
    LEFT_TIME = 'leftTime'
    BASE_TIME = 'baseTime'
    TIME_MULTIPLIER = 1000
    CHARGE_TIME_MULTIPLIER = 1000
    CHANGE_GUN_TRANSITION_TIME = 0.4

class ReloadFactorsState(object):
    __slots__: tuple
    __flags: Any
    def __init__(self):
        ...
    def __ior__(self, other):
        ...
    def __iand__(self, other):
        ...
    def cleanup(self):
        ...
    def hasNegativeEffect(self):
        ...

class ReloadingAffectPolicy(object):
    __slots__: tuple
    __stateID: Any
    __reloadingFactors: Any
    def __init__(self, reloadingFactors, stateID):
        ...
    def __call__(self, value):
        ...
    def _updateFactors(self, value):
        ...

class DeviceAffectPolicy(ReloadingAffectPolicy):
    __AFFECT_DEVICES: tuple
    __AFFECT_STATES: tuple
    def __call__(self, value):
        ...

class DestroyStateAffectPolicy(ReloadingAffectPolicy):
    __AFFECT_STATES: tuple
    __AFFECT_LEVEL: tuple
    def __call__(self, value):
        ...

class StunAffectPolicy(ReloadingAffectPolicy):
    def __call__(self, value):
        ...

class DualGunComponent(DualGunPanelMeta, IPrebattleSetupsListener):
    __sessionProvider: Any
    __reloadingState: Any
    __deviceStateHandlers: Any
    __isEnabled: Any
    __isObservingVehicle: Any
    __isAllowedByContext: Any
    __chargeState: Any
    __prevChargeState: Any
    __deferredGunState: Any
    __bulletCollapsed: Any
    __debuffInProgress: Any
    __debuffBaseTime: Any
    __inBattle: Any
    __reloadEventReceived: Any
    __isObserver: Any
    __currentTotalTimeTimer: Any
    __soundManager: Any
    def __init__(self):
        ...
    def updateVehicleParams(self, vehicle, factors):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onVehicleStateUpdated(self, stateID, value):
        ...
    def __onPostMortemSwitched(self, noRespawnPossible, respawnAvailable):
        ...
    def __onSpectatorModeChanged(self, mode):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __onCrosshairPositionChanged(self, *_):
        ...
    def __onArenaPeriodChange(self, arenaPeriod, endTime, *_):
        ...
    def __onVehicleControlling(self, vehicle):
        ...
    @staticmethod
    def _convertServerStateToUI(state):
        ...
    def __onBattleStarted(self):
        ...
    def __updateContextAvailability(self):
        ...
    def __updateGunState(self, gunID, state, serverCooldownData):
        ...
    def __onVehicleFeedbackReceived(self, eventID, vehicleID, value):
        ...
    def __onCameraChanged(self, cameraName, currentVehicleId=None):
        ...
    def __onDualGunStateUpdated(self, value):
        ...
    @staticmethod
    def __getTimeUntilNextDoubleShot(cooldownTimes):
        ...
    def __updateDualGunState(self, states, cooldownTimes):
        ...
    def __onPreCharge(self, _):
        ...
    def __onControlModeChange(self, event):
        ...
    def __chargeReleased(self, event):
        ...
    def __onDualGunChargeStateUpdated(self, value):
        ...
    def __updateChargeTimerState(self, *args):
        ...
    def __onReplayTimeWarpStart(self):
        ...
    def __onReplayPause(self, _):
        ...
    def __updateTimeUntilNextDoubleShot(self, increaseByDebuff=False):
        ...
    def __isPlayerVehicle(self):
        ...
    # decorador original: @noexceptReturn(...)
    def __isVisible(self):
        ...
