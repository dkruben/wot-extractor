# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/MinimapGrid.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/MinimapGrid.py
from __future__ import absolute_import
import weakref
from gui.Scaleform.daapi.view.meta.MinimapGridMeta import MinimapGridMeta
from helpers import dependency
from skeletons.account_helpers.settings_core import ISettingsCore

class MinimapGrid(MinimapGridMeta):
    settingsCore = dependency.descriptor(ISettingsCore)

    def __init__(self):
        super(MinimapGrid, self).__init__()
        self._channel = None
        self._controller = None
        self.__mapId = 0
        return

    def setController(self, controller):
        controller.activate()
        self._controller = weakref.ref(controller)

    def removeController(self):
        self._controller = lambda : None

    def setActive(self, isActive):
        self.as_clickEnabledS(isActive)

    def setClick(self, x, y):
        controller = self._controller()
        if controller:
            command = controller.proto.unitChat.createByMapPos(x, y)
            controller.sendCommand(command)

    def setMapId(self, mapId):
        if mapId != self.__mapId:
            self.as_clearPointsS()
        self.__mapId = mapId

    def addCommand(self, cmd):
        if cmd.isOnMinimap():
            self.as_addPointS(cmd.getMapPosX(), cmd.getMapPosY())

    def as_addMessageS(self, message):
        pass

    def as_setJoinedS(self, flag):
        pass
