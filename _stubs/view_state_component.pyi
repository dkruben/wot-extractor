# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/view_state_component.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from cache import cached_property as cached_property
from constants import BuffDisplayedState as BuffDisplayedState
from gui.battle_control.battle_constants import FEEDBACK_EVENT_ID as FEEDBACK_EVENT_ID, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import MarkersManagerEvent as MarkersManagerEvent
from helpers import dependency as dependency
from helpers.fixed_dict import getTimeInterval as getTimeInterval
from script_component.DynamicScriptComponent import DynamicScriptComponent as DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers.fixed_dict import TimeInterval as TimeInterval
_VIEW_STATE_UPDATERS: dict

class ViewStateComponent(DynamicScriptComponent):
    _viewStateUpdater: Any
    def __init__(self, *args, **kwargs):
        ...
    def onDestroy(self):
        ...
    def set_isActive(self, prev):
        ...
    def set_timeInterval(self, prev):
        ...
    def _onAvatarReady(self):
        ...
    def _invalidateViewState(self):
        ...

class ViewStateComponentAdaptor(object):
    __entity: Any
    __state: Any
    __viewStateUpdater: Any
    def __init__(self, entity, state):
        ...
    @property
    def entity(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def timeInterval(self):
        ...
    @property
    def isSourceVehicle(self):
        ...
    def updateState(self, state):
        ...
    def destroy(self):
        ...
    def __invalidateViewState(self):
        ...

class ViewStateUpdater(object):
    _FEEDBACK_EVENT_ID = None
    _VEHICLE_VIEW_STATE = None
    _component: Any
    _vehicleID: Any
    _isActive: Any
    def __init__(self, component):
        ...
    # decorador original: @cached_property
    def _sessionProvider(self):
        ...
    # decorador original: @cached_property
    def _vehicleStateCtrl(self):
        ...
    @property
    def _controllingVehicleID(self):
        ...
    def onVehicleControlling(self, vehicle):
        ...
    def invalidate(self, _=None):
        ...
    def destroy(self):
        ...
    def _invalidateState(self):
        ...
    def _getState(self):
        ...

class _AoeInspireStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_AOE_INSPIRE
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.AOE_INSPIRE
    def _getState(self):
        ...

class _AoeHealStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_AOE_HEAL
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.AOE_HEAL
    def _getState(self):
        ...

class _RiskyAttackBuffStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_RISKY_ATTACK_BUFF
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.RISKY_ATTACK_BUFF

class _RiskyAttackHealStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_RISKY_ATTACK_HEAL
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.RISKY_ATTACK_HEAL

class _BerserkStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_BERSERK
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.BERSERK

class _SniperStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_SNIPER
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.SNIPER

class _HunterStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_HUNTER
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.HUNTER

class _FastRechargeStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_FAST_RECHARGE
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.FAST_RECHARGE

class _AllySupportStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_ALLY_SUPPORT
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.ALLY_SUPPORT

class _JuggernautStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_JUGGERNAUT
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.JUGGERNAUT

class _SureShotStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_SURE_SHOT
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.SURE_SHOT

class _ConcentrationStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_CONCENTRATION
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.CONCENTRATION

class _MarchStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_MARCH
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.MARCH

class _AggressiveDetectionStateUpdater(ViewStateUpdater):
    _FEEDBACK_EVENT_ID = FEEDBACK_EVENT_ID.VEHICLE_AGGRESSIVE_DETECTION
    _VEHICLE_VIEW_STATE = VEHICLE_VIEW_STATE.AGGRESSIVE_DETECTION

def _viewStateUpdaterFactory(stateID, component):
    ...
