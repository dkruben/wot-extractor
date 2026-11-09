# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/lobby_notifier.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/comp7_core/gui/Scaleform/daapi/view/battle/lobby_notifier.py
from __future__ import absolute_import
import BigWorld
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from constants import ARENA_PERIOD
_NOTIFICATION_TIME = 20.0

class LobbyNotifier(IAbstractPeriodView):

    def __init__(self):
        super(LobbyNotifier, self).__init__()
        self.__isNotified = False

    def setCountdown(self, state, timeLeft):
        if state == ARENA_PERIOD.PREBATTLE and timeLeft <= _NOTIFICATION_TIME:
            self.__doNotify()

    def __doNotify(self):
        if not self.__isNotified:
            BigWorld.WGWindowsNotifier.onBattleBeginning()
            self.__isNotified = True
