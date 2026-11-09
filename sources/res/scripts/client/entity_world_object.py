# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/entity_world_object.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/entity_world_object.py
from __future__ import absolute_import
import BigWorld

class EntityWorldObject(BigWorld.Entity):

    def __init__(self):
        self.worldObject = None
        return

    def onEnterWorld(self, *args):
        self.worldObject = self._loadWorldObject()

    def onLeaveWorld(self):
        if self.worldObject is not None:
            self.worldObject.deactivate()
            self.worldObject.destroy()
            self.worldObject.stopLoading = True
            self.worldObject = None
        return

    def _loadWorldObject(self):
        raise NotImplementedError

    def _registerWorldObject(self, worldObject):
        self.worldObject = worldObject
        self.worldObject.setMotor(self.matrix)
        self.worldObject.activate()
