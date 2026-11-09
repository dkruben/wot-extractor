# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/stance_dance_fight_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from constants import ARENA_PERIOD as ARENA_PERIOD
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from helpers import dependency as dependency
from gui.Scaleform.daapi.view.meta.StanceDanceFightWidgetMeta import StanceDanceFightWidgetMeta as StanceDanceFightWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.crosshair_type_updater import CrosshairTypeUpdater as CrosshairTypeUpdater
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.replay_paused_view_updater import ReplayPausedViewUpdater as ReplayPausedViewUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import List as List, Tuple as Tuple
from StanceDanceController import StanceDanceState as StanceDanceState
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeyCommand as HotKeyCommand
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class StanceDanceFightMechanicWidget(StanceDanceFightWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    _HOT_KEY_MAP: dict
    __sessionProvider: Any
    __isPaused: Any
    __progress: Any
    __uiState: Any
    __defaultKey: Any
    __activeKey: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, _, newState):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    def setHotkeys(self, hotKeyCommands):
        ...
    def onReplayPaused(self, isPaused):
        ...
    def _getViewUpdaters(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onArenaPeriodChange(self, arenaPeriod, *_):
        ...
    def __invalidateKey(self):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
    def __invalidateProgress(self, state, uiState):
        ...

def _getWidgetState(prev, state):
    ...
