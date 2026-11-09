# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/EntityVisualScriptRunner.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/EntityVisualScriptRunner.py
from __future__ import absolute_import
import zlib
from future.moves import pickle
import BigWorld
from script_component.DynamicScriptComponent import DynamicScriptComponent
from visual_script_client.contexts.vehicle_context import VehicleContextClient
from visual_script_client.contexts.entity_context import EntityContextClient

class EntityVisualScriptRunner(DynamicScriptComponent):

    def __init__(self):
        super(EntityVisualScriptRunner, self).__init__()
        self._vsePlans = None
        self._ctx = None
        return

    def _onAvatarReady(self):
        if self.clientPlan:
            player = BigWorld.player()
            arenaInfo = player.arena.arenaInfo
            self._vsePlans = vsePlans = arenaInfo.visualScriptCache.getPlan(self.keyName, [self.clientPlan])
            if self.entity.__class__.__name__ == 'Vehicle':
                self._ctx = VehicleContextClient(self.entity)
            else:
                self._ctx = EntityContextClient(self)
            clientPlanParams = pickle.loads(zlib.decompress(self.clientPlanParams))
            vsePlans.setContext(self._ctx)
            vsePlans.setOptionalInputParams(**clientPlanParams)
            vsePlans.start()

    def onDestroy(self):
        if self._vsePlans is not None:
            self._vsePlans.stop()
        if self._ctx is not None:
            self._ctx.destroy()
        self._vsePlans = None
        self._ctx = None
        super(EntityVisualScriptRunner, self).onDestroy()
        return
