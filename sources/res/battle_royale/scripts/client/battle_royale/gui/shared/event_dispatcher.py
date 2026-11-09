# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/shared/event_dispatcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/shared/event_dispatcher.py
from __future__ import absolute_import
from skeletons.gui.impl import IGuiLoader
from gui.impl.pub.notification_commands import WindowNotificationCommand
from helpers import dependency
from skeletons.gui.impl import INotificationWindowController

def showBattleRoyaleResults(ctx):
    from battle_royale.gui.impl.lobby.views.states import BattleRoyaleBattleResultsState
    BattleRoyaleBattleResultsState.goTo(**ctx)


def showHangar():
    from battle_royale.gui.impl.lobby.views.states import BattleRoyaleHangarState
    BattleRoyaleHangarState.goTo()


@dependency.replace_none_kwargs(guiLoader=IGuiLoader)
def showInfoPage(isModeSelector=False, guiLoader=None):
    from battle_royale.gui.impl.lobby.views.info_page import InfoPageWindow
    view = guiLoader.windowsManager.getViewByLayoutID(InfoPageWindow.LAYOUT_ID)
    if view is None:
        window = InfoPageWindow(isModeSelector)
        window.load()
    return


def showBattleRoyalePrimeTime():
    from battle_royale.gui.impl.lobby.views.states import BattleRoyalePrimeTimeState
    BattleRoyalePrimeTimeState.goTo()


def showHangarVehicleConfigurator():
    from battle_royale.gui.impl.lobby.views.states import BattleRoyaleVehicleInfoState
    BattleRoyaleVehicleInfoState.goTo()


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showAwardsView(stage, notificationMgr=None):
    from battle_royale.gui.impl.lobby.views.battle_quest_awards_view import BattleQuestAwardsViewWindow
    window = BattleQuestAwardsViewWindow(stage)
    notificationMgr.append(WindowNotificationCommand(window))


def showProgressionView(activeTab=None):
    from battle_royale.gui.impl.lobby.views.states import BattleRoyaleProgressionState
    from battle_royale.gui.impl.gen.view_models.views.lobby.views.progression.progression_main_view_model import MainViews
    if not activeTab:
        activeTab = MainViews.PROGRESSION
    BattleRoyaleProgressionState.goTo(ctx={'menuName': activeTab})
