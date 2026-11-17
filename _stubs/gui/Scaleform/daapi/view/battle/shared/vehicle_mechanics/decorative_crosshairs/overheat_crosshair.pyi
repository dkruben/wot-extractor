# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/overheat_crosshair.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BattleReplay as BattleReplay
from ReplayEvents import g_replayEvents as g_replayEvents
from constants import OVERHEAT_GAIN_STATE as OVERHEAT_GAIN_STATE
from events_containers.common.containers import ContainersListener as ContainersListener
from gui.veh_mechanics.battle.updaters.current_shell_damage_updater import CurrentShellDamageUpdater as CurrentShellDamageUpdater
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.OverheatDecorativeCrosshairMeta import OverheatDecorativeCrosshairMeta as OverheatDecorativeCrosshairMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from math_common import round_py2_style_int as round_py2_style_int
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from typing import List as List, Optional as Optional
from OverheatStacksController import OverheatStacksState as OverheatStacksState
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class OverheatDecorativeCrosshair(OverheatDecorativeCrosshairMeta, ContainersListener, IMechanicStatesListenerLogic):
    __progress: Any
    __level: Any
    __baseDamage: Any
    __maxLevel: Any
    __speedThreshold: Any
    __dmgLevelBonus: Any
    __heatingTime: Any
    __coolingTime: Any
    __delayTimerProgress: Any
    __gainState: Any
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
    def updateTimersData(self, speed):
        ...
    def onCurrentShellDamageChanged(self, newDamage):
        ...
    def _getViewUpdaters(self):
        ...
    def _onReplayTimeWarpFinished(self):
        ...
    def _onPlaybackSpeedChanged(self, speed):
        ...
    def __updateState(self, state):
        ...
    def __updateExpectedDamage(self, newBaseDamage=None):
        ...
    def __invalidateState(self, state):
        ...
    def __invalidateExpectedDamage(self, newDamage):
        ...
    def __invalidateAll(self, state, force=False):
        ...
    def __sendProgressToAS(self):
        ...
