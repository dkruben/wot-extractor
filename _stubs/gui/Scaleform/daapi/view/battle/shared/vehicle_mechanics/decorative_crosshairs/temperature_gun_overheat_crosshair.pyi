# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/temperature_gun_overheat_crosshair.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import OVERHEAT_GUN_STATE as OVERHEAT_GUN_STATE
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.TemperatureGunOverheatDecorativeCrosshairMeta import TemperatureGunOverheatDecorativeCrosshairMeta as TemperatureGunOverheatDecorativeCrosshairMeta
from gui.Scaleform.genConsts.DECORATIVE_CROSSHAIR_CONSTS import DECORATIVE_CROSSHAIR_CONSTS as DECORATIVE_CROSSHAIR_CONSTS
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import IOverheatGunMechanicState as IOverheatGunMechanicState
_MECHANIC_STATE_DECOR_MAP: dict

class TemperatureGunOverheatDecorativeCrosshair(TemperatureGunOverheatDecorativeCrosshairMeta, ContainersListener, IMechanicStatesListenerLogic):
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, _, newState):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateState(self, overheatState, isInstantly=False):
        ...
