# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/mechanic_widgets/charge_shot_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import CommandMapping as CommandMapping
from events_containers.common.containers import ContainersListener as ContainersListener
from events_containers.components.life_cycle import IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from events_handler import eventHandler as eventHandler
from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import HotKeyData as HotKeyData
from gui.Scaleform.daapi.view.meta.ChargeShotWidgetMeta import ChargeShotWidgetMeta as ChargeShotWidgetMeta
from gui.Scaleform.genConsts.MECHANICS_WIDGET_CONST import MECHANICS_WIDGET_CONST as MECHANICS_WIDGET_CONST
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR as CANT_SHOOT_ERROR
from gui.veh_mechanics.battle.updaters.hotkey_updaters import HotKeysViewUpdater as HotKeysViewUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_life_cycle_updater import VehicleMechanicLifeCycleUpdater as VehicleMechanicLifeCycleUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater as VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater as VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.current_shell_damage_updater import CurrentShellDamageUpdater as CurrentShellDamageUpdater
from gui.veh_mechanics.battle.updaters.shot_blocked_upater import ShotBlockedUpdater as ShotBlockedUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from math_common import round_py2_style_int as round_py2_style_int
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic
from typing import List as List, Optional as Optional
from ChargeShotComponent import ChargeShotState as ChargeShotState
from items.components.shared_components import ChargeShotParams as ChargeShotParams
from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater as IViewUpdater

class ChargeShotMechanicWidget(ChargeShotWidgetMeta, ContainersListener, IMechanicStatesListenerLogic, IComponentLifeCycleListenerLogic):
    _HOT_KEY_MAP: dict
    __damageFactorsPerLevel: Any
    __expectedDamage: Any
    __baseDamage: Any
    __level: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateTransition(self, _, newState):
        ...
    # decorador original: @eventHandler
    def onStateTick(self, state):
        ...
    # decorador original: @eventHandler
    def onComponentParamsCollected(self, params):
        ...
    def onCurrentShellDamageChanged(self, newDamage):
        ...
    def onShotBlocked(self, error):
        ...
    def _getViewUpdaters(self):
        ...
    def __invalidateAll(self, state, isInstantly=False):
        ...
    def __invalidateProgress(self, state):
        ...
    def __updateExpectedDamage(self, newBaseDamage=None):
        ...
    def __invalidateExpectedDamage(self, newDamage):
        ...
