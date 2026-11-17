# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/easy_equip_entry_sub_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.easy_tank_equip.easy_tank_equip_helpers import isAvailableForVehicle as isAvailableForVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel as VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries import isVehicleUnavailable as isVehicleUnavailable
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter as BaseMenuEntrySubPresenter
from gui.prb_control.entities.base.listener import IPrbListener as IPrbListener
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from gui.shared.event_dispatcher import showEasyTankEquipScreen as showEasyTankEquipScreen
from helpers import dependency as dependency
from skeletons.gui.game_control import IEasyTankEquipController as IEasyTankEquipController, IPlatoonController as IPlatoonController
NOT_FULL_QS_AMMO_MULTILIER = 0.8

class EasyEquipEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __easyTankEquipCtrl: Any
    __platoonCtrl: Any
    def onNavigate(self):
        ...
    def _getEvents(self):
        ...
    def _getListeners(self):
        ...
    def _getState(self):
        ...
    @staticmethod
    def __isAmmoNotFull():
        ...
    def __onSettingsChange(self):
        ...
    def __onPlatoonMembersUpdate(self, *_):
        ...
    def __onPrbEntitySwitched(self, _):
        ...
    def __onCameraEnabledChange(self, _):
        ...
