# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/Radar.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/Radar.py
from __future__ import absolute_import
import BigWorld, CGF
from Math import Vector3
import BattleReplay
from helpers import dependency
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider

class Radar(BigWorld.DynamicScriptComponent):
    __dynObjectsCache = dependency.descriptor(IBattleDynamicObjectsCache)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onEnterWorld(self, *args):
        pass

    def onLeaveWorld(self, *args):
        pass

    def set_radarReadinessTime(self, _=None):
        radarCtrl = self.entity.guiSessionProvider.dynamic.radar
        if radarCtrl:
            radarCtrl.updateRadarReadinessTime(self.radarReadinessTime)

    def set_radarReady(self, prev=None):
        radarCtrl = self.entity.guiSessionProvider.dynamic.radar
        if radarCtrl:
            radarCtrl.updateRadarReadiness(self.radarReady)

    def refreshRadar(self):
        self.set_radarReadinessTime()
        self.set_radarReady()

    def activatePatrickEffect(self):
        if BattleReplay.g_replayCtrl.isPlaying and BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        self.__playEffect()

    def __playEffect(self):
        prefabPath = self.__dynObjectsCache.getConfig(self.__sessionProvider.arenaVisitor.getArenaGuiType()).getStPatrickLootEffect().prefabs[0]
        CGF.loadGameObjectIntoHierarchy(prefabPath, self.entity.entityGameObject, Vector3(0))
