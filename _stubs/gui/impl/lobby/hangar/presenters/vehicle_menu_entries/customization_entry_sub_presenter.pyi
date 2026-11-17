# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/customization_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries import isVehicleUnavailable as isVehicleUnavailable
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter as BaseMenuEntrySubPresenter
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency, server_settings as server_settings
from items.components.c11n_constants import ItemTags as ItemTags
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IPlatoonController as IPlatoonController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class CustomizationEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __customizationService: Any
    __itemsCache: Any
    __lobbyContext: Any
    __platoonCtrl: Any
    def onNavigate(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getState(self):
        ...
    def __onPrbEntitySwitched(self, _):
        ...
    def __onPlatoonMembersUpdate(self, *_):
        ...
    # decorador original: @server_settings.serverSettingsChangeListener(...)
    def __onServerSettingChanged(self, _):
        ...
    def __onCameraEnabledChange(self, _):
        ...
