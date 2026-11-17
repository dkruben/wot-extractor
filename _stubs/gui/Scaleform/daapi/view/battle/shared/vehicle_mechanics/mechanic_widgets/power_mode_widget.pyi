# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/power_mode_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import POWER_MODE_STATE as POWER_MODE_STATE
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.PowerWidgetMeta import PowerWidgetMeta as PowerWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from PowerModeController import PowerModeState as PowerModeState
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class PowerModeMechanicWidget(PowerWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    _POWER_MODE_UI_STATES: dict
    __progress: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
    def __invalidateProgress(self, state, forced=False):
        ...
