# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/wheeled_dash_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from cache import last_cached_method as last_cached_method
from WheeledDashController import WheeledDashState as WheeledDashState
from constants import PHASED_MECHANIC_STATE as PHASED_MECHANIC_STATE
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.WheeledDashWidgetMeta import WheeledDashWidgetMeta as WheeledDashWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from helpers import dependency as dependency
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_commands_updater import VehicleMechanicCommandsUpdater as VehicleMechanicCommandsUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class WheeledDashMechanicWidget(WheeledDashWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    __sessionProvider: Any
    _WHEELED_DASH_UI_STATES: dict
    _HOT_KEY_MAP: dict
    __progressUpdaters: Any
    __isReducedCooldown: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getViewUpdaters(self):
        ...
    def __getDisplayState(self, state):
        ...
    def __invalidateState(self, state, isInstantly=False):
        ...
    # decorador original: @last_cached_method(...)
    def __invalidateProgress(self, uiState, progress, timeLeft, baseTime, isReducedCooldown):
        ...
