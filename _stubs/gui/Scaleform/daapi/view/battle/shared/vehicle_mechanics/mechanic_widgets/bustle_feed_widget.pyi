# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/bustle_feed_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from constants import BUSTLE_FEED_STATE as BUSTLE_FEED_STATE, BUSTLE_FEED_SWITCH_ACCESS as BUSTLE_FEED_SWITCH_ACCESS
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.BustleFeedWidgetMeta import BustleFeedWidgetMeta as BustleFeedWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_commands_updater import VehicleMechanicCommandsUpdater as VehicleMechanicCommandsUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_commands import IMechanicCommandsListenerLogic as IMechanicCommandsListenerLogic
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from vehicles.mechanics.generic_mechanics.bustle_feed import BustleFeedState as BustleFeedState

class BustleFeedMechanicWidget(BustleFeedWidgetMeta, ContainersListener, IMechanicStatesListenerLogic, IMechanicCommandsListenerLogic):
    _BUSTLE_FEED_UI_STATES: dict
    _HOT_KEY_MAP: dict
    __switchAccessState: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    # decorador original: @eventHandler
    def onMechanicCommand(self, command):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
    def __invalidateState(self, state, isInstantly=False):
        ...
    def __invalidateAvailability(self, state):
        ...
    def __invalidateProgress(self, state):
        ...
