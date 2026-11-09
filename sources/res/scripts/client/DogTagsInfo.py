# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/DogTagsInfo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/DogTagsInfo.py
from __future__ import absolute_import
import typing, BigWorld, Event
if typing.TYPE_CHECKING:
    from typing import List, Tuple

class DogTagsInfo(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(DogTagsInfo, self).__init__()
        self.__eManager = Event.EventManager()
        self.onUsedComponentsUpdated = Event.Event(self.__eManager)

    def onLeaveWorld(self, *args):
        self.__eManager.clear()

    def setSlice_usedDogTagsComponents(self, changePath, oldValue):
        begin, end = changePath[0]
        newComponents = self.usedDogTagsComponents[begin:end]
        self.onUsedComponentsUpdated(newComponents)
