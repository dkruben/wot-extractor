# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/AvatarBattleRoyaleComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/AvatarBattleRoyaleComponent.py
from __future__ import absolute_import
import BigWorld
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
import BattleReplay
from BattleReplay import g_replayEvents
from Event import EventsSubscriber

class AvatarBattleRoyaleComponent(BigWorld.DynamicScriptComponent, EventsSubscriber):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(AvatarBattleRoyaleComponent, self).__init__()
        if BattleReplay.g_replayCtrl.isPlaying:
            BattleReplay.g_replayCtrl.useSyncroniusResourceLoading(True)
            self.subscribeToEvent(g_replayEvents.onTimeWarpStart, self.__onTimeWarpStart)
            self.subscribeToEvent(g_replayEvents.onTimeWarpFinish, self.__onTimeWarpFinish)

    def onLeaveWorld(self):
        self.unsubscribeFromAllEvents()

    def set_playerPlace(self, _prev):
        self.sessionProvider.arenaVisitor.getComponentSystem().battleRoyaleComponent.setBattleRoyalePlace(self.playerPlace)

    def __onTimeWarpStart(self):
        BigWorld.worldDrawEnabled(False)

    def __onTimeWarpFinish(self):
        BigWorld.worldDrawEnabled(True)
