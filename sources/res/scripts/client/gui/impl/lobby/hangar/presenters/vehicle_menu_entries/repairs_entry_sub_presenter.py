# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/repairs_entry_sub_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/repairs_entry_sub_presenter.py
from __future__ import absolute_import
import adisp
from CurrentVehicle import g_currentVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter
from gui.impl.lobby.tank_setup.dialogs.main_content.main_contents import NeedRepairMainContent
from gui.impl.lobby.tank_setup.dialogs.need_repair import NeedRepair
from gui.prb_control.entities.base.listener import IPrbListener
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.gui_items.items_actions.actions import VehicleRepairAction
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController

class RepairsEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __platoonCtrl = dependency.descriptor(IPlatoonController)

    def onNavigate(self):
        self.__handleRepair()

    def _getEvents(self):
        return (
         (
          self.__platoonCtrl.onMembersUpdate, self.__onPlatoonMembersUpdate),
         (
          self._cameraController.onEnabledChange, self.__onCameraEnabledChange))

    def _getListeners(self):
        return (
         (
          events.PrebattleEvent.SWITCHED, self.__onPrbEntitySwitched, EVENT_BUS_SCOPE.LOBBY),)

    def _getState(self):
        if g_currentVehicle.isBroken():
            return VehicleMenuModel.CRITICAL
        if g_currentVehicle.isInBattle() or g_currentVehicle.isLocked():
            return VehicleMenuModel.DISABLED
        return VehicleMenuModel.ENABLED

    @adisp.adisp_process
    def __handleRepair(self):
        if g_currentVehicle.isPresent():
            vehicle = g_currentVehicle.item
            yield VehicleRepairAction(vehicle, NeedRepair, NeedRepairMainContent).doAction()

    def __onPlatoonMembersUpdate(self, *_):
        self.packEntry()

    def __onPrbEntitySwitched(self, _):
        self.packEntry()

    def __onCameraEnabledChange(self, _):
        self.packEntry()
