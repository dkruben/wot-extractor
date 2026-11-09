# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/Scaleform/daapi/view/lobby/__init__.py
from __future__ import absolute_import
from gui.Scaleform.framework import WindowLayer, ScopeTemplates, ViewSettings
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES
from gui.app_loader.settings import APP_NAME_SPACE
from gui.shared.event_bus import EVENT_BUS_SCOPE
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES

def getStateMachineRegistrators():
    from fun_random.gui.Scaleform.daapi.view.lobby.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getContextMenuHandlers():
    return ()


def getViewSettings():
    from fun_random.gui.Scaleform.daapi.view.lobby.feature.prime_time_view import FunRandomPrimeTimeView
    return (
     ViewSettings(FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME, FunRandomPrimeTimeView, HANGAR_ALIASES.RANKED_PRIME_TIME, WindowLayer.SUB_VIEW, FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME, ScopeTemplates.LOBBY_SUB_SCOPE, True),)


def getBusinessHandlers():
    return (
     FunRandomLobbyBusinessHandler(),)


class FunRandomLobbyBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          FUNRANDOM_ALIASES.FUN_RANDOM_PRIME_TIME, self.loadViewByCtxEvent),)
        super(FunRandomLobbyBusinessHandler, self).__init__(listeners, APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
