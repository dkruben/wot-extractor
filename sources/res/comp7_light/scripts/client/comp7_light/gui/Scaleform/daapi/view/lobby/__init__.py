# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/__init__.py
from __future__ import absolute_import
from comp7_light.gui.Scaleform.genConsts.COMP7_LIGHT_HANGAR_ALIASES import COMP7_LIGHT_HANGAR_ALIASES
from comp7_core.gui.Scaleform.genConsts.COMP7_CORE_HANGAR_ALIASES import COMP7_CORE_HANGAR_ALIASES
from gui.Scaleform.framework import WindowLayer, ScopeTemplates, ViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared.event_bus import EVENT_BUS_SCOPE

def getContextMenuHandlers():
    return ()


def getViewSettings():
    from comp7_light.gui.impl.lobby.hangar.comp7_light_hangar import Comp7LightHangarWindow
    from comp7_light.gui.Scaleform.daapi.view.lobby.comp7_light_prime_time_view import Comp7LightPrimeTimeView
    from gui.Scaleform.framework import getSwfExtensionUrl
    from comp7_light.gui.impl.lobby.battle_results.comp7_light_battle_results_view import Comp7LightBattleResultsWindow
    return (
     ViewSettings(COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_BATTLE_RESULTS, Comp7LightBattleResultsWindow, '', WindowLayer.SUB_VIEW, COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_BATTLE_RESULTS, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_PRIME_TIME_ALIAS, Comp7LightPrimeTimeView, getSwfExtensionUrl('comp7_core', COMP7_CORE_HANGAR_ALIASES.COMP7_CORE_PRIME_TIME_SWF), WindowLayer.SUB_VIEW, COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_PRIME_TIME_ALIAS, ScopeTemplates.LOBBY_SUB_SCOPE, True),
     ViewSettings(COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_LOBBY_HANGAR, Comp7LightHangarWindow, '', WindowLayer.SUB_VIEW, COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_LOBBY_HANGAR, ScopeTemplates.LOBBY_SUB_SCOPE))


def getBusinessHandlers():
    return (
     Comp7LightHangarBusinessHandler(),)


class Comp7LightHangarBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_PRIME_TIME_ALIAS, self.loadViewByCtxEvent),
         (
          COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_LOBBY_HANGAR, self.loadViewByCtxEvent),
         (
          COMP7_LIGHT_HANGAR_ALIASES.COMP7_LIGHT_BATTLE_RESULTS, self.loadViewByCtxEvent))
        super(Comp7LightHangarBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
