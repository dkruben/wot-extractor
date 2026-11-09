# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/repairs_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import adisp as adisp
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter as BaseMenuEntrySubPresenter
from gui.impl.lobby.tank_setup.dialogs.main_content.main_contents import NeedRepairMainContent as NeedRepairMainContent
from gui.impl.lobby.tank_setup.dialogs.need_repair import NeedRepair as NeedRepair
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items.items_actions.actions import VehicleRepairAction as VehicleRepairAction
from helpers import dependency as dependency
from skeletons.gui.game_control import IPlatoonController as IPlatoonController

class RepairsEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __platoonCtrl: Any
    def onNavigate(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getState(self):
        ...
    # decorador original: @adisp.adisp_process
    def __handleRepair(self):
        ...
    def __onPlatoonMembersUpdate(self, *_):
        ...
    def __onPrbEntitySwitched(self, _):
        ...
    def __onCameraEnabledChange(self, _):
        ...
