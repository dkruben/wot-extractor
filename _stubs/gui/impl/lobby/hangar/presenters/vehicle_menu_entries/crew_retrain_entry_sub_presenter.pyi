# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/crew_retrain_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.dialogs.dialogs import showRetrainMassiveDialog as showRetrainMassiveDialog
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries import isVehicleUnavailable as isVehicleUnavailable
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter as BaseMenuEntrySubPresenter
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.gui_items.Vehicle import getLowEfficiencyTankmenIDs as getLowEfficiencyTankmenIDs
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from skeletons.gui.shared import IItemsCache as IItemsCache

class CrewRetrainEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __itemsCache: Any
    __platoonCtrl: Any
    __hasInventoryTankman: Any
    def __init__(self, name, viewModel, parentView):
        ...
    def packEntry(self):
        ...
    def onNavigate(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getState(self):
        ...
    def __handleCrewRetrain(self):
        ...
    def __onPlatoonMembersUpdate(self, *_):
        ...
    def __onPrbEntitySwitched(self, _):
        ...
    def __onCameraEnabledChange(self, _):
        ...
