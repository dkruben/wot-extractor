# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/pve_base/pve_player_lives.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/pve_base/pve_player_lives.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.meta.PvePlayerLivesMeta import PvePlayerLivesMeta
from gui.battle_control import avatar_getter
from TeamInfoLivesComponent import TeamInfoLivesComponent

class PvePlayerLives(PvePlayerLivesMeta):

    def _populate(self):
        super(PvePlayerLives, self)._populate()
        teamLives = TeamInfoLivesComponent.getInstance()
        if teamLives is not None:
            teamLives.onTeamLivesUpdated += self._onTeamLivesUpdated
        self._updateRespawnInfo()
        return

    def _dispose(self):
        teamLives = TeamInfoLivesComponent.getInstance()
        if teamLives is not None:
            teamLives.onTeamLivesUpdated -= self._onTeamLivesUpdated
        super(PvePlayerLives, self)._dispose()
        return

    def _updateRespawnInfo(self):
        teamLives = TeamInfoLivesComponent.getInstance()
        if not teamLives:
            return
        playerVehicleID = avatar_getter.getPlayerVehicleID()
        lives = teamLives.getLives(playerVehicleID)
        usedLives = teamLives.getUsedLives(playerVehicleID)
        lockedLives = teamLives.getLockedLives(playerVehicleID)
        self.as_setCountLivesS(lives, usedLives, lockedLives)

    def _onTeamLivesUpdated(self):
        self._updateRespawnInfo()
