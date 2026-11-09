# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/store/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/last_stand/gui/scaleform/daapi/view/lobby/store/__init__.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from last_stand.gui import ls_gui_constants

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.Scaleform.daapi.view.lobby.store.browser.shop_view import ShopOverlay
    from gui.Scaleform.framework import ViewSettings, ScopeTemplates
    return (
     ViewSettings(ls_gui_constants.VIEW_ALIAS.LS_OVERLAY_WEB_STORE, ShopOverlay, 'browserScreen.swf', WindowLayer.OVERLAY, ls_gui_constants.VIEW_ALIAS.LS_OVERLAY_WEB_STORE, ScopeTemplates.LOBBY_SUB_SCOPE),)


def getBusinessHandlers():
    return (
     StorePackageBusinessHandler(),)


class StorePackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          ls_gui_constants.VIEW_ALIAS.LS_OVERLAY_WEB_STORE, self.loadViewByCtxEvent),)
        super(StorePackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
