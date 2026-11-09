# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/compare_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter as BaseMenuEntrySubPresenter
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket

class CompareEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __cmpBasket: Any
    def onNavigate(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getState(self):
        ...
    def __handleCompare(self):
        ...
    def __onCmpBasketChange(self, *_):
        ...
    def __onVehCmpBasketStateChanged(self):
        ...
    def __onPrbEntitySwitched(self, _):
        ...
    def __onCameraEnabledChange(self, _):
        ...
