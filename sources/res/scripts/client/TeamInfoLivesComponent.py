# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/TeamInfoLivesComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/TeamInfoLivesComponent.py
from __future__ import absolute_import
import BigWorld, Event
from helpers import isPlayerAvatar
from script_component.DynamicScriptComponent import DynamicScriptComponent

class TeamInfoLivesComponent(DynamicScriptComponent):

    def __init__(self, *_, **__):
        super(TeamInfoLivesComponent, self).__init__(*_, **__)
        self.onTeamLivesUpdated = Event.SafeEvent()

    def onDestroy(self):
        self.onTeamLivesUpdated.clear()
        super(TeamInfoLivesComponent, self).onDestroy()

    def _onAvatarReady(self):
        self.onTeamLivesUpdated()

    def set_teamLives(self, prev):
        if self._isAvatarReady:
            self.onTeamLivesUpdated()

    def getLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get('lives', 0)

    def getLockedLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get('lockedLives', 0)

    def getUsedLives(self, vehicleID):
        return self.getVehicleLives(vehicleID).get('usedLives', 0)

    def getVehicleLives(self, vehicleID):
        for vl in self.teamLives:
            if vl['vehicleID'] == vehicleID:
                return dict(vl)

        return {}

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
            return getattr(player.arena.teamInfo, 'teamLivesComponent', None)
