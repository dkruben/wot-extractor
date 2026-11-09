# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/TeamInfo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/TeamInfo.py
from __future__ import absolute_import
import BigWorld
from debug_utils import LOG_DEBUG_DEV
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class TeamInfo(BigWorld.Entity):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onCombatEquipmentUsed(self, vehicleID, equipmentID):
        self.__sessionProvider.shared.equipments.onCombatEquipmentUsed(vehicleID, equipmentID)

    def onEnterWorld(self, prereqs):
        LOG_DEBUG_DEV(('[TeamInfo] onEnterWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.registerTeamInfo(self)

    def onLeaveWorld(self):
        LOG_DEBUG_DEV(('[TeamInfo] onLeaveWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.unregisterTeamInfo(self)

    def onDynamicComponentCreated(self, component):
        LOG_DEBUG_DEV('Component created', component)

    def showHittingArea(self, equipmentID, hittingPoint, hittingDirection, hittingTime):
        BigWorld.player().showHittingArea(equipmentID, hittingPoint, hittingDirection, hittingTime)
