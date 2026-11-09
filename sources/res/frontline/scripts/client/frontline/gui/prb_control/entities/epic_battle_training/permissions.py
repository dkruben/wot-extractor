# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/prb_control/entities/epic_battle_training/permissions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/prb_control/entities/epic_battle_training/permissions.py
from __future__ import absolute_import
from constants import PREBATTLE_ROLE
from gui.prb_control.entities.base.legacy.permissions import LegacyPermissions, ILegacyPermissions

class EpicBattleTrainingPermissions(LegacyPermissions):

    def canChangeVehicle(self):
        return True

    def canCreateSquad(self):
        return False

    @classmethod
    def isCreator(cls, roles):
        return roles == PREBATTLE_ROLE.TRAINING_CREATOR

    def canChangeSetting(self):
        return self.canChangeComment() or self.canChangeArena() or self.canMakeOpenedClosed()

    def canStartBattle(self):
        return self.canSetTeamState(1) and self.canSetTeamState(2)


class EpicBattleTrainingIntroPermissions(ILegacyPermissions):

    def canCreateSquad(self):
        return False
