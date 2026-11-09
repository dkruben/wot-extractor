# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ArenaObserverInfo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ArenaObserverInfo.py
from __future__ import absolute_import
import BigWorld
from debug_utils import LOG_DEBUG_DEV
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class ArenaObserverInfo(BigWorld.Entity):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onEnterWorld(self, prereqs):
        BigWorld.player().arena.registerArenaObserverInfo(self)

    def onLeaveWorld(self):
        BigWorld.player().arena.unregisterArenaObserverInfo(self)

    def onDynamicComponentCreated(self, component):
        LOG_DEBUG_DEV('Component created', component)
