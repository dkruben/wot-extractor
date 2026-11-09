# wot-extractor: codigo DESCOMPILADO de sources/res/fun_random/scripts/client/fun_random/gui/shared/event_dispatcher.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: fun_random/scripts/client/fun_random/gui/shared/event_dispatcher.py
from __future__ import absolute_import
from frameworks.wulf import WindowLayer
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS
from gui.impl.gen import R
from gui.impl.pub.notification_commands import WindowNotificationCommand
from gui.shared.event_dispatcher import showBrowserOverlayView, showModeSelectorWindow
from helpers import dependency
from skeletons.gui.impl import IGuiLoader, INotificationWindowController

def showFunRandomPrimeTimeWindow(subModeID):
    from fun_random.gui.Scaleform.daapi.view.lobby.states import FunRandomPrimeTimeState
    FunRandomPrimeTimeState.goTo(ctx={'subModeID': subModeID})


def showFunRandomProgressionWindow():
    from fun_random.gui.impl.lobby.feature.states import FunRandomProgressionState
    FunRandomProgressionState.goTo()


def showFunRandomTierList(parent=None):
    from fun_random.gui.impl.lobby.feature.states import FunRandomTierListState
    FunRandomTierListState.goTo(parent=parent)


def showFunRandomBattleResults(arenaUniqueID, subModeImpl):
    from fun_random.gui.impl.lobby.feature.states import FunPostBattleResultsState
    FunPostBattleResultsState.goTo(arenaUniqueID=arenaUniqueID, subModeImpl=subModeImpl)


def showFunRandomInfoPage(infoPageUrl):
    showBrowserOverlayView(infoPageUrl, VIEW_ALIAS.WEB_VIEW_TRANSPARENT, hiddenLayers=(
     WindowLayer.MARKER, WindowLayer.VIEW, WindowLayer.WINDOW))


@dependency.replace_none_kwargs(uiLoader=IGuiLoader)
def showFunRandomModeSubSelectorWindow(uiLoader=None):
    contentResId = R.views.lobby.mode_selector.ModeSelectorView()
    if uiLoader.windowsManager.getViewByLayoutID(contentResId) is None:
        showModeSelectorWindow(subSelectorCallback=showFunRandomSubSelector)
    else:
        showFunRandomSubSelector()
    return


@dependency.replace_none_kwargs(uiLoader=IGuiLoader)
def showFunRandomSubSelector(parent=None, uiLoader=None):
    from fun_random.gui.impl.lobby.mode_selector.states import FunRandomSubSelectorState
    contentResId = R.views.lobby.mode_selector.ModeSelectorView()
    parent = parent or uiLoader.windowsManager.getViewByLayoutID(contentResId).getParentWindow()
    FunRandomSubSelectorState.goTo(parent=parent)


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showFunRandomLootBoxAwardWindow(data, notificationMgr=None):
    from fun_random.gui.impl.lobby.feature.fun_random_rewards_view import FunRandomLootBoxAwardWindow
    notificationMgr.append(WindowNotificationCommand(FunRandomLootBoxAwardWindow(data)))
