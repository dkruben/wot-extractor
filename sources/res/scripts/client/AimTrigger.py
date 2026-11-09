# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AimTrigger.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AimTrigger.py
from __future__ import absolute_import
import BigWorld, TriggersManager

class AimTrigger(BigWorld.UserDataObject):

    def __init__(self):
        BigWorld.UserDataObject.__init__(self)
        self.__id = TriggersManager.g_manager.addTrigger(TriggersManager.TRIGGER_TYPE.AIM, name=self.name, position=self.position, radius=self.radius, maxDistance=self.maxDistance)

    def destroy(self):
        TriggersManager.g_manager.delTrigger(self.__id)
