# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/low_charge_shot_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
from constants import LowChargeShotReloadingState as LowChargeShotReloadingState
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.LowChargeShotWidgetMeta import LowChargeShotWidgetMeta as LowChargeShotWidgetMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.mechanics.low_charge_shot_updater import LowChargeShotUpdater as LowChargeShotUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.gun_mechanics.low_charge_shot.private import LowChargeShotMechanicState as LowChargeShotMechanicState, DEFAULT_MECHANIC_STATE as DEFAULT_MECHANIC_STATE
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class LowChargeShotMechanicWidget(LowChargeShotWidgetMeta, ContainersListener, IMechanicStatesListenerLogic):
    __mechanicState: Any
    __shellChangeTime: Any
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
    def setShellChangeTime(self, isVisible, shellChangeTimes):
        ...
    def setBaseTimeBeforeBattleOrEmpty(self, baseTimeSet):
        ...
    def _getViewUpdaters(self):
        ...
    def __updateState(self, state):
        ...
    def __updateShellChangeTime(self, shellChangeTimes):
        ...
    def __updateTimeLeft(self, timeLeft, state):
        ...
    def __updateInitialTime(self):
        ...
