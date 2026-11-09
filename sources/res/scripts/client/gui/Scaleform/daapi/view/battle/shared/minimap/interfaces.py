# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/minimap/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/minimap/interfaces.py
from __future__ import absolute_import
import typing
from abc import abstractmethod
if typing.TYPE_CHECKING:
    from account_helpers.settings_core.settings_constants import GAME
    from aih_constants import CTRL_MODE_NAME

class IMinimapPlugin(typing.Protocol):

    @abstractmethod
    def applyNewSize(self, sizeIndex):
        raise NotImplementedError

    @abstractmethod
    def updateControlMode(self, mode, vehicleID):
        raise NotImplementedError

    @abstractmethod
    def initControlMode(self, mode, available):
        raise NotImplementedError

    @abstractmethod
    def updateSettings(self, diff):
        raise NotImplementedError

    @abstractmethod
    def setSettings(self):
        raise NotImplementedError
