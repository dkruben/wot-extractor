# wot-extractor: codigo DESCOMPILADO de sources/res/in_battle_achievements/scripts/client/VehicleAchievementsComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: in_battle_achievements/scripts/client/VehicleAchievementsComponent.py
from __future__ import absolute_import
import logging, BigWorld
from dossiers2.custom.records import DB_ID_TO_RECORD as ID2NAME
logger = logging.getLogger(__name__)

class VehicleAchievementsComponent(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(VehicleAchievementsComponent, self).__init__()
        logger.debug('[IN_BATTLE_ACHIEVEMENTS] VehicleAchievementsComponent has been initialized')

    def setSlice_achievements(self, changePath, oldValue):
        logger.debug('[IN_BATTLE_ACHIEVEMENTS] self.setSlice_achievements: achievements: %s, changePath: %s', self.achievements, changePath)
        startIndex, endIndex = changePath[-1]
        receivedAchievements = self.achievements[startIndex:endIndex]
        revokedAchievements = oldValue
        logger.debug('[IN_BATTLE_ACHIEVEMENTS] Received: %s - Revoked: %s', (', ').join([ID2NAME[item][1] for item in receivedAchievements if item in ID2NAME]), (', ').join([ID2NAME[item][1] for item in revokedAchievements if item in ID2NAME]))
