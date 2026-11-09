# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/autoreloader_surge_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from constants import ARENA_PERIOD as ARENA_PERIOD, AUTORELOADER_SURGE_RESTRICTION as AUTORELOADER_SURGE_RESTRICTION, AUTORELOADER_SURGE_STATE as AUTORELOADER_SURGE_STATE
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.Scaleform.daapi.view.meta.AutoreloaderSurgeWidgetMeta import AutoreloaderSurgeWidgetMeta as AutoreloaderSurgeWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.crosshair_type_updater import CrosshairTypeUpdater as CrosshairTypeUpdater
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_life_cycle_updater import VehicleMechanicLifeCycleUpdater as VehicleMechanicLifeCycleUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from helpers import dependency as dependency
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from typing import List as List
from AutoreloaderSurgeController import AutoreloaderSurgeState as AutoreloaderSurgeState
from items.components.shared_components import AutoreloaderSurgeParams as AutoreloaderSurgeParams
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
_STATE_MAP: dict

class AutoreloaderSurgeMechanicWidget(AutoreloaderSurgeWidgetMeta, ContainersListener, IComponentLifeCycleListenerLogic, IMechanicStatesListenerLogic):
    _HOT_KEY_MAP: dict
    __sessionProvider: Any
    __maxCharges: Any
    __startCharges: Any
    __chargeTimeSFullClip: Any
    __chargeTimeSRegular: Any
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
    def onStateTransition(self, _, newState):
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
    def __onArenaPeriodChange(self, arenaPeriod, *_):
        ...
    def __getReloadTimeLeft(self):
        ...
    def __getWidgetState(self, state):
        ...
    def __buildStagesProgress(self, state):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
