# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/impl/lobby/feature/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/impl/lobby/feature/__init__.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.app_loader import settings as app_settings
from gui.Scaleform.genConsts.FUNRANDOM_ALIASES import FUNRANDOM_ALIASES
from gui.Scaleform.framework import ViewSettings
from gui.Scaleform.framework import ScopeTemplates
from gui.Scaleform.framework.package_layout import PackageBusinessHandler
from gui.shared import EVENT_BUS_SCOPE

def getStateMachineRegistrators():
    from fun_random.gui.impl.lobby.feature.states import registerStates, registerTransitions
    return (
     registerStates, registerTransitions)


def getContextMenuHandlers():
    return ()


def getViewSettings():
    from fun_random.gui.impl.lobby.feature.fun_random_battle_results_view import FunPostBattleResultsWindow
    from fun_random.gui.impl.lobby.feature.fun_random_progression_view import FunRandomProgressionWindow
    return (
     ViewSettings(FUNRANDOM_ALIASES.FUN_POST_BATTLE_RESULTS, FunPostBattleResultsWindow, '', WindowLayer.SUB_VIEW, FUNRANDOM_ALIASES.FUN_POST_BATTLE_RESULTS, ScopeTemplates.LOBBY_SUB_SCOPE),
     ViewSettings(FUNRANDOM_ALIASES.FUN_PROGRESSION, FunRandomProgressionWindow, '', WindowLayer.SUB_VIEW, FUNRANDOM_ALIASES.FUN_PROGRESSION, ScopeTemplates.LOBBY_SUB_SCOPE))


def getBusinessHandlers():
    return (
     FunRandomBusinessHandler(),)


class FunRandomBusinessHandler(PackageBusinessHandler):

    def __init__(self):
        listeners = (
         (
          FUNRANDOM_ALIASES.FUN_POST_BATTLE_RESULTS, self.loadView),
         (
          FUNRANDOM_ALIASES.FUN_PROGRESSION, self.loadView))
        super(FunRandomBusinessHandler, self).__init__(listeners, app_settings.APP_NAME_SPACE.SF_LOBBY, EVENT_BUS_SCOPE.LOBBY)
