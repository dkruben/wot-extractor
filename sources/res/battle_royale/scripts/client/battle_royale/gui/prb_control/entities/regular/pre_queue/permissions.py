# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/permissions.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/battle_royale/gui/prb_control/entities/regular/pre_queue/permissions.py
from __future__ import absolute_import
from gui.prb_control.entities.base.pre_queue.permissions import PreQueuePermissions
from helpers import time_utils, dependency
from gui.periodic_battles.models import PrimeTimeStatus
from skeletons.gui.game_control import IBattleRoyaleController

class BattleRoyalePermissions(PreQueuePermissions):
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)

    def canCreateSquad(self):
        currentSeason = self.__battleRoyaleController.getCurrentSeason()
        status, _, _ = self.__battleRoyaleController.getPrimeTimeStatus()
        if status != PrimeTimeStatus.AVAILABLE:
            return False
        if currentSeason and super(BattleRoyalePermissions, self).canCreateSquad():
            if currentSeason.hasActiveCycle(time_utils.getCurrentLocalServerTimestamp()):
                return True
        return False
