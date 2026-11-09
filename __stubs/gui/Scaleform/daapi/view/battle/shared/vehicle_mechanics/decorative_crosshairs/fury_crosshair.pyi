# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/fury_crosshair.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
from ReplayEvents import g_replayEvents as g_replayEvents
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.FuryDecorativeCrosshairMeta import FuryDecorativeCrosshairMeta as FuryDecorativeCrosshairMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from typing import List as List
from BattleFuryController import BattleFuryState as BattleFuryState
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class FuryDecorativeCrosshair(FuryDecorativeCrosshairMeta, ContainersListener, IMechanicStatesListenerLogic):
    __level: Any
    __progress: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    def _getViewUpdaters(self):
        ...
    def __onReplayTimeWarpFinished(self):
        ...
    def __invalidateState(self, state):
        ...
