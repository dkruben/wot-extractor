# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/lootbox_system/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/lootbox_system/__init__.py
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE

def getStateMachineRegistrators():
    from gui.impl.lobby.lootbox_system.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getContextMenuHandlers():
    return ()


def getViewSettings():
    from gui.impl.lobby.lootbox_system.base.intro_browser_view import LootBoxSystemIntroBrowserView
    from gui.impl.lobby.lootbox_system.base.info_page import InfoPageWindow
    from gui.impl.lobby.lootbox_system.base.main_view import MainWindow
    from gui.impl.lobby.lootbox_system.base.auto_open_view import AutoOpenWindow
    return (
     ViewSettings(VIEW_ALIAS.LOOT_BOXES_INTRO_BROWSER_VIEW, LootBoxSystemIntroBrowserView, 'browserScreen.swf', WindowLayer.OVERLAY, VIEW_ALIAS.LOOT_BOXES_INTRO_BROWSER_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.LOOT_BOXES_INFO_VIEW, InfoPageWindow, '', WindowLayer.TOP_WINDOW, VIEW_ALIAS.LOOT_BOXES_INFO_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.LOOT_BOXES_MAIN_VIEW, MainWindow, '', WindowLayer.TOP_WINDOW, VIEW_ALIAS.LOOT_BOXES_MAIN_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(VIEW_ALIAS.LOOT_BOXES_AUTO_OPEN_VIEW, AutoOpenWindow, '', WindowLayer.TOP_WINDOW, VIEW_ALIAS.LOOT_BOXES_AUTO_OPEN_VIEW, ScopeTemplates.LOBBY_SUB_SCOPE))


def getBusinessHandlers():
    return (
     LootBoxSystemPackageBusinessHandler(),)


class LootBoxSystemPackageBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.LOOT_BOXES_INTRO_BROWSER_VIEW, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.LOOT_BOXES_INFO_VIEW, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.LOOT_BOXES_MAIN_VIEW, self.loadViewByCtxEvent),
         (
          VIEW_ALIAS.LOOT_BOXES_AUTO_OPEN_VIEW, self.loadViewByCtxEvent))
        super(LootBoxSystemPackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
