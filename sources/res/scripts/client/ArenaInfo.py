# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ArenaInfo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ArenaInfo.py
from __future__ import absolute_import
import BigWorld
from cgf_script.entity_dyn_components import BWEntitiyComponentTracker
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
ARENA_INFO_COMPONENTS = {}

class ArenaInfo(BigWorld.Entity, BWEntitiyComponentTracker):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        for comp in ARENA_INFO_COMPONENTS:
            comp.__init__(self)

    def set_planeTrajectory(self, _):
        avatar = BigWorld.player()
        if self.planeTrajectory and avatar.userSeesWorld():
            avatar.updatePlaneTrajectory(self.planeTrajectory)

    def showCarpetBombing(self, equipmentID, position, hittingDirection, time):
        avatar = BigWorld.player()
        if avatar is not None:
            avatar.showCarpetBombing(equipmentID, position, hittingDirection, time)
        return

    def onEnterWorld(self, prereqs):
        for comp in ARENA_INFO_COMPONENTS:
            comp.onEnterWorld(self)

        arena = BigWorld.player().arena
        if arena:
            arena.registerArenaInfo(self)

    def onLeaveWorld(self):
        for comp in ARENA_INFO_COMPONENTS:
            comp.onLeaveWorld(self)

        BigWorld.player().arena.unregisterArenaInfo(self)
