# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/temp_overheat_gun_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from cache import last_cached_method as last_cached_method
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.meta.TemperatureGunOverheatWidgetMeta import TemperatureGunOverheatWidgetMeta as TemperatureGunOverheatWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as _UI_STATES
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_life_cycle_updater import VehicleMechanicLifeCycleUpdater as VehicleMechanicLifeCycleUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.temp_overheat_gun_updater import ITemperatureOverheatGunStatesListenerLogic as ITemperatureOverheatGunStatesListenerLogic, TemperatureOverheatGunStatesUpdater as TemperatureOverheatGunStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import DEFAULT_TEMPERATURE_MECHANIC_STATE as DEFAULT_TEMPERATURE_MECHANIC_STATE
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import DEFAULT_OVERHEAT_MECHANIC_STATE as DEFAULT_OVERHEAT_MECHANIC_STATE
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun import IOverheatGunComponentParams as IOverheatGunComponentParams, IOverheatGunMechanicState as IOverheatGunMechanicState
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState as ITemperatureGunMechanicState

class TemperatureOverheatGunWidget(TemperatureGunOverheatWidgetMeta, ContainersListener, IComponentLifeCycleListenerLogic, ITemperatureOverheatGunStatesListenerLogic):
    __tempState: Any
    __overheatState: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onComponentParamsCollected(self, params):
        ...
    # decorador original: @eventHandler
    def onOverheatStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onOverheatStateTransition(self, prevState, newState):
        ...
    # decorador original: @eventHandler
    def onTemperatureStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onTemperatureStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onTemperatureStateTick(self, state):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateAll(self, tempState, overheatState, isInstantly=False):
        ...
    # decorador original: @last_cached_method(...)
    def __invalidateProgresses(self, temperatureProgress, overheatTime):
        ...
