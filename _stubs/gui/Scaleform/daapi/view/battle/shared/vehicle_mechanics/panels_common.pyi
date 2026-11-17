# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/panels_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Dict as Dict, Iterable as Iterable, Tuple as Tuple, TYPE_CHECKING as TYPE_CHECKING
import BattleReplay as BattleReplay
from events_containers.common.containers import ContainersListener as ContainersListener
from events_handler import eventHandler as eventHandler
from gui.battle_control.battle_constants import CROSSHAIR_VIEW_ID as CROSSHAIR_VIEW_ID
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent as BaseDAAPIComponent
from gui.veh_mechanics.battle.updaters.mechanics.tracked_mechanics_updater import IVehicleTrackedMechanicsView as IVehicleTrackedMechanicsView, VehicleTrackedMechanicsUpdater as VehicleTrackedMechanicsUpdater
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdatersCollection as ViewUpdatersCollection
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey

class VehicleMechanicsPanel(BaseDAAPIComponent, ContainersListener, IVehicleTrackedMechanicsView):
    __sessionProvider: Any
    _VEHICLE_MECHANIC_UI_COMPONENTS_MAP: dict
    __updatersCollection: Any
    __crosshairViewID: Any
    __isAllowedByContext: Any
    __isRadialMenuOpened: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onTrackedMechanicsUpdate(self, mechanics):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _destroy(self):
        ...
    def _setIsReplay(self, isReplay):
        ...
    def _setIsVisible(self, isVisible):
        ...
    def _setCrosshairScaledPosition(self, position):
        ...
    def _setCrosshairViewID(self, viewID):
        ...
    def _addMechanicUIComponents(self, mechanicComponents):
        ...
    def __onRadialMenuOpenChanged(self):
        ...
    def __onBattleStarted(self):
        ...
    def __onCrosshairScaledPositionChanged(self, *_):
        ...
    def __onCrosshairViewChanged(self, viewID):
        ...
    def __updateRadialMenuOpened(self):
        ...
    def __updateContextAvailability(self):
        ...
    def __updateCrosshairViewID(self, viewID):
        ...
    def __updateVisibility(self):
        ...

def _getMechanicsUIComponents(vehicleMechanics, componentsMap):
    ...
