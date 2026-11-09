# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/frameworks/wulf/windows_system/windows_area.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/frameworks/wulf/windows_system/windows_area.py
from __future__ import absolute_import
import typing
from .window import Window
from ..gui_constants import PositionAnchor
from ..py_object_binder import PyObjectEntity
from ..py_object_wrappers import PyObjectWindowsArea

class WindowsArea(PyObjectEntity):
    __slots__ = ()

    def __init__(self):
        super(WindowsArea, self).__init__(cppObject=PyObjectWindowsArea())

    @property
    def areaID(self):
        proxy = self.proxy
        if proxy is not None:
            return proxy.areaID
        else:
            return 0

    def addWindow(self, window):
        return self.proxy.addPyWindow(window.proxy)

    def removeWindow(self, window):
        return self.proxy.removePyWindow(window.proxy)

    def getFirstWindow(self):
        return self.proxy.getFirstPyWindow()

    def getLastWindow(self):
        return self.proxy.getLastPyWindow()

    def getPreviousNeighbor(self, window):
        return self.proxy.getPreviousPyNeighbor(window.uniqueID)

    def getNextNeighbor(self, window):
        return self.proxy.getNextPyNeighbor(window.uniqueID)

    def move(self, window, x, y, xAnchor=PositionAnchor.LEFT, yAnchor=PositionAnchor.TOP):
        return self.proxy.movePyWindow(window.uniqueID, x, y, xAnchor, yAnchor)

    def center(self, window):
        return self.proxy.centerPyWindow(window.uniqueID)

    def cascade(self, window):
        return self.proxy.cascadePyWindow(window.uniqueID)
