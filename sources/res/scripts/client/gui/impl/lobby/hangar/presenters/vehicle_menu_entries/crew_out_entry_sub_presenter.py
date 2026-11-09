# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/crew_out_entry_sub_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/hangar/presenters/vehicle_menu_entries/crew_out_entry_sub_presenter.py
from __future__ import absolute_import
import BigWorld
from CurrentVehicle import g_currentVehicle
from gui.impl.gen.view_models.views.lobby.hangar.vehicle_menu_model import VehicleMenuModel
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries import isVehicleUnavailable
from gui.impl.lobby.hangar.presenters.vehicle_menu_entries.base_menu_entry_sub_presenter import BaseMenuEntrySubPresenter
from gui.prb_control.entities.base.listener import IPrbListener
from gui.shared import events, EVENT_BUS_SCOPE
from gui.shared.gui_items.items_actions import factory
from helpers import dependency
from skeletons.gui.game_control import IPlatoonController
from skeletons.gui.shared import IItemsCache

class CrewOutEntrySubPresenter(BaseMenuEntrySubPresenter, IPrbListener):
    __itemsCache = dependency.descriptor(IItemsCache)
    __platoonCtrl = dependency.descriptor(IPlatoonController)

    def __init__(self, name, viewModel, parentView):
        super(CrewOutEntrySubPresenter, self).__init__(name, viewModel, parentView)
        self.__hasInventoryTankman = False

    def packEntry(self):
        self.__hasInventoryTankman = bool(self.__itemsCache.items.getInventoryTankmen(limit=1))
        super(CrewOutEntrySubPresenter, self).packEntry()

    def onNavigate(self):
        self.__handleCrewOut()

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
        if not self.__hasInventoryTankman:
            return VehicleMenuModel.DISABLED
        if not g_currentVehicle.isPresent():
            return VehicleMenuModel.DISABLED
        if g_currentVehicle.item.isCrewLocked:
            return VehicleMenuModel.DISABLED
        if not g_currentVehicle.hasCrew() or isVehicleUnavailable():
            return VehicleMenuModel.DISABLED
        return VehicleMenuModel.ENABLED

    def __handleCrewOut(self):
        vehicle = g_currentVehicle.item
        actions = [(factory.UNLOAD_TANKMAN, vehicle.invID, slotIdx) for slotIdx, tmanInvId in vehicle.crew if tmanInvId is not None]
        BigWorld.player().doActions(actions)
        return

    def __onPlatoonMembersUpdate(self, *_):
        self.packEntry()

    def __onPrbEntitySwitched(self, _):
        self.packEntry()

    def __onCameraEnabledChange(self, _):
        self.packEntry()
