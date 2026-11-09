# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/armor_inspector_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from armor_inspector_common.schemas import armorInspectorConfigSchema as armorInspectorConfigSchema
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter as BaseMenuEntrySubPresenter
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.event_dispatcher import showVehicleHubArmor as showVehicleHubArmor

class ArmorInspectorEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    def onNavigate(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getState(self):
        ...
    def __configChangeHandler(self, gpKey):
        ...
    def __onPrbEntitySwitched(self, _):
        ...
    def __onCameraEnabledChange(self, _):
        ...
