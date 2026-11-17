# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/sight_pointer_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import ARENA_PERIOD as ARENA_PERIOD, SIGHT_POINTER_STATE as SIGHT_POINTER_STATE, SIGHT_POINTER_COMMON_CONSTANTS as SIGHT_POINTER_COMMON_CONSTANTS
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.Scaleform.daapi.view.meta.SightPointerWidgetMeta import SightPointerWidgetMeta as SightPointerWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_life_cycle_updater import VehicleMechanicLifeCycleUpdater as VehicleMechanicLifeCycleUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from items.components.shared_components import SightPointerParams as SightPointerParams
from SightPointerComponent import SightPointerState as SightPointerState

class SightPointerMechanicWidget(SightPointerWidgetMeta, ContainersListener, IComponentLifeCycleListenerLogic, IMechanicStatesListenerLogic):
    __sessionProvider: Any
    _UI_STATE_MAP: dict
    _HOT_KEY_MAP: dict
    __uiState: Any
    __progress: Any
    __tankIconState: Any
    __initialDeployTime: Any
    __isPrebattle: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onComponentParamsCollected(self, params):
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
    def _onSightPointerEnemySpotted(self):
        ...
    def __onArenaPeriodChange(self, arenaPeriod, *_):
        ...
    def __invalidateState(self, state, isInstantly=False):
        ...
    def __invalidateTankIcon(self, state):
        ...
    def __invalidateProgress(self, state, forced=False):
        ...
