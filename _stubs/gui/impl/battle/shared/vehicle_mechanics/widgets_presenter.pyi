# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/battle/shared/vehicle_mechanics/widgets_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from events_handler import eventHandler as eventHandler
from gui.battle_control.controllers.vehicle_passenger import hasVehiclePassengerCtrl as hasVehiclePassengerCtrl, VehiclePassengerInfoWatcher as VehiclePassengerInfoWatcher
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.veh_mechanics.battle.updaters.mechanics.tracked_mechanics_updater import IVehicleTrackedMechanicsView as IVehicleTrackedMechanicsView, VehicleTrackedMechanicsUpdater as VehicleTrackedMechanicsUpdater
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdatersCollection as ViewUpdatersCollection
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from frameworks.wulf import ViewModel as ViewModel
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
_WIDGET_ALIASES_BY_MECHANIC: dict

class VisibilityState(object):
    DEFAULT = 0
    IN_POSTMORTEM = 1
    @staticmethod
    def validate(state, value):
        ...

class VehicleMechanicsWidgetsPresenter(ViewComponent, VehiclePassengerInfoWatcher, IVehicleTrackedMechanicsView):
    __sessionProvider: Any
    __updatersCollection: Any
    __visibilityState: Any
    def __init__(self):
        ...
    # decorador original: @eventHandler
    def onTrackedMechanicsUpdate(self, mechanics):
        ...
    @property
    def viewModel(self):
        ...
    def _getChildComponents(self):
        ...
    def _getEvents(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    # decorador original: @hasVehiclePassengerCtrl(...)
    def __onVehicleControlling(self, _, passengerCtrl=None):
        ...
    def __onSwitchToPostmortem(self, _, __):
        ...
    def __enableComponent(self, value, resId):
        ...
