# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/clan_supply/clan_supply_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/clan_supply/clan_supply_helpers.py
import typing
from gui.impl.pub.notification_commands import WindowNotificationCommand
from helpers import dependency
from skeletons.gui.impl import INotificationWindowController

def showClanSupplyView(tabId=None, *args, **kwargs):
    from gui.impl.lobby.clan_supply.states import ClanSupplyState
    ClanSupplyState.goTo(tabId=tabId)


@dependency.replace_none_kwargs(notificationMgr=INotificationWindowController)
def showClanSupplyRewardWindow(isElite, rewards, notificationMgr=None):
    from gui.impl.lobby.clan_supply.rewards_view import RewardsViewWindow
    window = RewardsViewWindow(isElite, rewards)
    notificationMgr.append(WindowNotificationCommand(window))
