# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/prb_control/entities/battle_session/legacy/permissions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/prb_control/entities/battle_session/legacy/permissions.py
from gui.prb_control import prb_getters
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions
from gui.prb_control.entities.base.limits import TeamNoPlayersInBattle, MaxCount

class BattleSessionPermissions(LegacyPermissions):

    def canSendInvite(self):
        return super(BattleSessionPermissions, self).canSendInvite() and self._canAddPlayers()

    def canExitFromQueue(self):
        return self.isCreator(self._roles)

    @classmethod
    def isCreator(cls, roles):
        return False

    def canAssignToTeam(self, team=1, isSelfAssignment=False):
        result = super(BattleSessionPermissions, self).canAssignToTeam(team, isSelfAssignment)
        if not result:
            return False
        else:
            clientPrb = prb_getters.getClientPrebattle()
            result = False
            if clientPrb is not None:
                settings = prb_getters.getPrebattleSettings(prebattle=clientPrb)
                rosters = prb_getters.getPrebattleRosters(prebattle=clientPrb)
                prbType = prb_getters.getPrebattleType(clientPrb, settings)
                result, _ = TeamNoPlayersInBattle(prbType).check(rosters, team, settings.getTeamLimits(team))
            return result

    def _canAddPlayers(self):
        clientPrb = prb_getters.getClientPrebattle()
        result = False
        if clientPrb is not None:
            settings = prb_getters.getPrebattleSettings(prebattle=clientPrb)
            rosters = prb_getters.getPrebattleRosters(prebattle=clientPrb)
            result, _ = MaxCount().check(rosters, 1, settings.getTeamLimits(1))
        return result
