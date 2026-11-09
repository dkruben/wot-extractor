# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/maps_training/arena_time_notificator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/maps_training/arena_time_notificator.py
from __future__ import absolute_import
from gui.battle_control.controllers.period_ctrl import IAbstractPeriodView
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
_TIME_TO_NOTIFY_BATTLE_END = 120

class MapsTrainingArenaTimeNotificator(IAbstractPeriodView):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(MapsTrainingArenaTimeNotificator, self).__init__()
        self.__prevLength = None
        self.__period = None
        self.__lastNotifiedTime = None
        return

    def setTotalTime(self, totalTime):
        if self.__lastNotifiedTime is None:
            self.__lastNotifiedTime = totalTime
        if totalTime == _TIME_TO_NOTIFY_BATTLE_END or totalTime < _TIME_TO_NOTIFY_BATTLE_END < self.__lastNotifiedTime:
            self.sessionProvider.dynamic.battleHints.showHint('maps_training.timeRunsOut', {'param1': _TIME_TO_NOTIFY_BATTLE_END})
        self.__lastNotifiedTime = totalTime
        return
