# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/avatar_stats_ctrl.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/avatar_stats_ctrl.py
from __future__ import absolute_import
import Event
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController

class AvatarStatsController(IBattleController):

    def __init__(self):
        super(AvatarStatsController, self).__init__()
        self.__stats = {}
        self.__eManager = Event.EventManager()
        self.onUpdated = Event.Event(self.__eManager)

    def getControllerID(self):
        return BATTLE_CTRL_ID.AVATAR_PRIVATE_STATS

    def startControl(self):
        pass

    def stopControl(self):
        self.__eManager.clear()
        self.__eManager = None
        return

    def getStats(self):
        return self.__stats

    def update(self, stats):
        self.__stats = stats
        self.onUpdated(stats)
