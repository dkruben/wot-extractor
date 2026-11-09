# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/notifications/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/notifications/__init__.py
from __future__ import absolute_import, division
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import GroupedViewSettings, ScopeTemplates, ComponentSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from notification.NotificationListView import NotificationListView
    from notification.NotificationPopUpViewer import NotificationPopUpViewer
    return (
     GroupedViewSettings(VIEW_ALIAS.NOTIFICATIONS_LIST, NotificationListView, 'notificationsList.swf', WindowLayer.WINDOW, 'notificationsList', VIEW_ALIAS.NOTIFICATIONS_LIST, ScopeTemplates.WINDOW_VIEWED_MULTISCOPE),
     ComponentSettings(VIEW_ALIAS.NOTIFICATION_VIEWER, NotificationPopUpViewer, ScopeTemplates.DEFAULT_SCOPE))


def getBusinessHandlers():
    return (
     NotificationsBusinessHandler(),)


class NotificationsBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.NOTIFICATIONS_LIST, self.loadViewByCtxEvent),)
        super(NotificationsBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
