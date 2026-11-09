# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/battle/random/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/battle/random/__init__.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.Scaleform.framework import ViewSettings, ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader import settings as app_settings
from gui.shared import EVENT_BUS_SCOPE
from .hud import RandomHUDWindow

def getContextMenuHandlers():
    return ()


def getViewSettings():
    return (
     ViewSettings(VIEW_ALIAS.RANDOM_BATTLE_HUD, RandomHUDWindow, '', WindowLayer.MARKER, None, ScopeTemplates.DEFAULT_SCOPE),)


def getBusinessHandlers():
    return (
     RandomBattlePackageBusinessHandler(),)


class RandomBattlePackageBusinessHandler(PackageBusinessHandler):
    __slots__ = ()

    def __init__(self):
        listeners = (
         (
          VIEW_ALIAS.RANDOM_BATTLE_HUD, self.loadViewByCtxEvent),)
        super(RandomBattlePackageBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_BATTLE, EVENT_BUS_SCOPE.BATTLE)
