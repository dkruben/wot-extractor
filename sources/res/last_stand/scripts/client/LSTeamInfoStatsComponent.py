# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSTeamInfoStatsComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSTeamInfoStatsComponent.py
from __future__ import absolute_import
import BigWorld, Event
from helpers import isPlayerAvatar

class LSTeamInfoStatsComponent(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(LSTeamInfoStatsComponent, self).__init__()
        self.onTeamStatsUpdated = Event.Event()
        self.onTeamHealthUpdated = Event.Event()

    def onDestroy(self):
        self.onTeamStatsUpdated.clear()
        self.onTeamHealthUpdated.clear()

    def getDamage(self, vehicleID):
        return self._getValue(self.damage, vehicleID)

    def getBlocked(self, vehicleID):
        return self._getValue(self.blocked, vehicleID)

    def getAssist(self, vehicleID):
        return self._getValue(self.assist, vehicleID)

    def getTeamSouls(self):
        return sum(info.value for info in self.souls)

    def getTeamHealth(self):
        return self.teamHealth

    def set_damage(self, prev):
        self.onTeamStatsUpdated()

    def set_blocked(self, prev):
        self.onTeamStatsUpdated()

    def set_assist(self, prev):
        self.onTeamStatsUpdated()

    def set_teamHealth(self, prev):
        self.onTeamHealthUpdated()

    @classmethod
    def getInstance(cls):
        if not isPlayerAvatar():
            return
        else:
            player = BigWorld.player()
            if not player:
                return
            if not player.arena or not player.arena.teamInfo:
                return
            return getattr(player.arena.teamInfo, cls.__name__, None)

    @staticmethod
    def _getValue(data, vehicleID, default=0):
        return next((info.value for info in data if info.id == vehicleID), default)
