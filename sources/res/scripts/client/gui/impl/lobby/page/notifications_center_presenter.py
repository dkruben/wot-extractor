# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/page/notifications_center_presenter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/page/notifications_center_presenter.py
from __future__ import absolute_import
from gui.impl.gen.view_models.views.lobby.page.footer.notifications_center_model import NotificationsCenterModel
from gui.impl.pub.view_component import ViewComponent
from gui.shared.notifications import NotificationPriorityLevel
from notification import NotificationMVC

class NotificationsCenterPresenter(ViewComponent[NotificationsCenterModel]):

    def __init__(self):
        super(NotificationsCenterPresenter, self).__init__(model=NotificationsCenterModel)

    @property
    def viewModel(self):
        return super(NotificationsCenterPresenter, self).getViewModel()

    def _initialize(self):
        super(NotificationsCenterPresenter, self)._initialize()
        NotificationMVC.g_instance.getModel().onNotifiedMessagesCountChanged += self.__onNotifiedMessagesCountChange
        NotificationMVC.g_instance.getModel().onNotificationReceived += self.__onNotificationReceived
        self.__updateNotifiedMessagesCount()

    def _finalize(self):
        model = NotificationMVC.g_instance.getModel()
        if model:
            model.onNotifiedMessagesCountChanged -= self.__onNotifiedMessagesCountChange
            model.onNotificationReceived -= self.__onNotificationReceived

    def __updateNotifiedMessagesCount(self):
        self.viewModel.setNewNotificationsCount(NotificationMVC.g_instance.getModel().getNotifiedMessagesCount())

    def __onNotifiedMessagesCountChange(self, _):
        self.__updateNotifiedMessagesCount()

    def __onNotificationReceived(self, notification):
        priorityLevel = notification.getPriorityLevel()
        self.viewModel.setHasImportantNotification(priorityLevel == NotificationPriorityLevel.HIGH)
