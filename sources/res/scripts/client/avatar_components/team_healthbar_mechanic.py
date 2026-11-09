# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/avatar_components/team_healthbar_mechanic.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/team_healthbar_mechanic.py
from __future__ import absolute_import
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as BONUS_CAPS

class TeamHealthbarMechanic(object):

    def __init__(self):
        self.__enabled = False
        self.__lastTeamHealthPercentage = None
        return

    def handleKey(self, isDown, key, mods):
        return False

    def onBecomePlayer(self):
        self.__enabled = self.hasBonusCap(BONUS_CAPS.TEAM_HEALTH_BAR)
        if not self.__enabled:
            return
        else:
            self.__lastTeamHealthPercentage = None
            return

    def onBecomeNonPlayer(self):
        if not self.__enabled:
            return
        else:
            self.__lastTeamHealthPercentage = None
            return

    def updateTeamsHealthPercentage(self, teamsHealthPercentage):
        if not self.__enabled:
            return
        self.__lastTeamHealthPercentage = teamsHealthPercentage
        self.arena.updateTeamHealthPercent(teamsHealthPercentage)

    def getHealthPercentage(self):
        return self.__lastTeamHealthPercentage
