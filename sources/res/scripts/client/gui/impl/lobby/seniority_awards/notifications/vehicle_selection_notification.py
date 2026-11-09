# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/seniority_awards/notifications/vehicle_selection_notification.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/seniority_awards/notifications/vehicle_selection_notification.py
from __future__ import absolute_import
from gui.impl.gen.view_models.views.lobby.seniority_awards.notifications.vehicle_selection_model import VehicleSelectionModel
from gui.impl.lobby.gf_notifications import NotificationBase
from gui.shared.event_dispatcher import showSeniorityRewardVehiclesWindow
from helpers import dependency
from skeletons.gui.game_control import ISeniorityAwardsController
from uilogging.seniority_awards.loggers import VehicleSelectionNotificationLogger

class VehicleSelectionNotification(NotificationBase):
    __seniorityAwardsController = dependency.descriptor(ISeniorityAwardsController)

    def __init__(self, resId, *args, **kwargs):
        super(VehicleSelectionNotification, self).__init__(resId, VehicleSelectionModel(), *args, **kwargs)
        self.__uiVehicleSelectionNotificationLogger = VehicleSelectionNotificationLogger()

    @property
    def viewModel(self):
        return self.getViewModel()

    def _getEvents(self):
        events = super(VehicleSelectionNotification, self)._getEvents()
        return events + (
         (
          self.viewModel.onClick, self.__onClick),
         (
          self.viewModel.onClose, self.__onClose))

    def _update(self):
        data = self._getPayload()
        with self.viewModel.transaction() as tx:
            tx.setIsPopUp(self._isPopUp)
            tx.setCount(data.get('count', 0))

    def __onClick(self):
        self.__uiVehicleSelectionNotificationLogger.handleClickAction()
        if self.__seniorityAwardsController.isVehicleSelectionAvailable:
            showSeniorityRewardVehiclesWindow()

    def __onClose(self):
        self.destroyWindow()
